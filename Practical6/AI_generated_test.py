'''import numpy as np
import matplotlib.pyplot as plt

def infect(array, beta1):
    """
    处理感染过程：将易感者（状态0）以概率beta1转为感染者（状态1）
    - array: 当前人群状态数组
    - beta1: 当前时间步的感染概率
    """
    # 找到所有易感者的索引
    susceptible_idx = np.where(array == 0)[0]
    # 根据beta1随机选择部分易感者感染
    infections = np.random.rand(len(susceptible_idx)) < beta1
    array[susceptible_idx[infections]] = 1  # 更新状态
    return array

def recover(array, gamma):
    """
    处理康复过程：感染者（状态1）以概率gamma转为康复者（状态2）
    - array: 当前人群状态数组
    - gamma: 康复概率
    """
    # 找到所有感染者的索引
    infected_idx = np.where(array == 1)[0]
    # 根据gamma随机选择部分感染者康复
    recoveries = np.random.rand(len(infected_idx)) < gamma
    array[infected_idx[recoveries]] = 2  # 更新状态
    return array

def betacount(array, beta, total_susceptible):
    """
    计算当前感染概率：beta * (感染者数 / 易感者总数)
    - array: 当前人群状态数组
    - beta: 基础感染率
    - total_susceptible: 当前易感者总数（含未感染的接种者）
    """
    current_infected = np.sum(array == 1)
    # 处理分母为0的情况（避免除以零错误）
    return beta * (current_infected / total_susceptible) if total_susceptible > 0 else 0

# 初始化绘图参数
plt.figure(figsize=(6,4), dpi=150)
N = 10000          # 总人口
beta = 0.3         # 基础感染率
gamma = 0.05       # 康复率
time_steps = 1000  # 模拟时间步数
x = list(range(time_steps + 1))  # 时间轴

# 遍历不同疫苗接种比例（0%, 10%, ..., 100%）
for vac_percent in range(0, 101, 10):
    vac_percent = vac_percent / 100.0  # 转换为小数（如10% → 0.1）
    vac_n = int(vac_percent * N)       # 计算接种者数量
    arr = np.zeros(N, dtype=int)       # 初始化状态数组（全为易感者0）
    
    # 设置接种者（状态3），前vac_n个位置标记为接种者
    arr[:vac_n] = 3
    remaining_susceptible = N - vac_n  # 剩余易感者数量
    
    # 初始感染者设置：从剩余易感者中随机选择一个
    if remaining_susceptible > 0:
        initial_infected = np.random.choice(np.where(arr == 0)[0], size=1)
        arr[initial_infected] = 1  # 设为感染者
    
    # 记录感染人数时间序列
    lst_inf = [np.sum(arr == 1)]  # 初始感染人数
    
    # 时间循环（每个时间步依次处理康复和感染）
    for _ in range(time_steps):
        arr = recover(arr, gamma)       # 先处理康复（状态1→2）
        # 计算当前易感者总数（状态0和3的总和）
        total_susceptible = np.sum((arr == 0) | (arr == 3))
        beta1 = betacount(arr, beta, total_susceptible)  # 计算感染概率
        arr = infect(arr, beta1)        # 再处理感染（状态0→1）
        lst_inf.append(np.sum(arr == 1))  # 记录当前感染人数
    
    # 将当前疫苗接种比例的感染曲线添加到图中
    plt.plot(x, lst_inf, label=f'{int(vac_percent*100)}%')

# 添加图表标签和图例
plt.xlabel('Time')
plt.ylabel('Infected')
plt.title('SIR Model with Vaccination (β=0.3, γ=0.05)')
plt.legend(title='Vaccination Rate')
plt.show()'''
import numpy as np
import matplotlib.pyplot as plt

def infect(array, beta1):
    """
    感染逻辑：仅易感者（状态0）可能被感染
    - beta1 已修正为基于总人口的感染概率
    """
    susceptible = (array == 0)  # 找到易感者
    infections = np.random.rand(len(array)) < beta1
    array[susceptible & infections] = 1  # 仅易感者被感染
    return array

def recover(array, gamma):
    """
    康复逻辑：感染者（状态1）以概率gamma康复
    """
    infected = (array == 1)
    recoveries = np.random.rand(len(array)) < gamma
    array[infected & recoveries] = 2  # 转为康复者
    return array

def betacount(beta, array, N):
    """
    修正感染概率计算：beta * (感染者数 / 总人口)
    - 避免因易感者过少导致概率爆炸
    """
    infected_count = np.sum(array == 1)
    return beta * (infected_count / N)  # 使用总人口作为分母

# 参数设置
plt.figure(figsize=(6,4), dpi=150)
N = 10000
beta = 0.3
gamma = 0.05
time = 1000  # 固定时间步数
x = list(range(time + 1))

# 明确指定需要模拟的 11 个疫苗接种比例
vaccination_rates = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 遍历指定的疫苗接种比例
for vac_percent in vaccination_rates:
    vac_percent = vac_percent / 100.0
    vac_n = int(vac_percent * N)
    arr = np.zeros(N, dtype=int)
    
    # 初始化疫苗接种者（状态3）
    arr[:vac_n] = 3
    remaining_susceptible = N - vac_n
    
    # 随机选择初始感染者（从易感者中）
    if remaining_susceptible > 0:
        susceptible_indices = np.where(arr == 0)[0]
        initial_infected = np.random.choice(susceptible_indices, 1)
        arr[initial_infected] = 1
    
    # 记录感染人数
    lst_inf = [np.sum(arr == 1)]
    
    # 时间循环（先处理康复，后处理感染）
    for _ in range(time):
        arr = recover(arr, gamma)          # 处理康复
        beta1 = betacount(beta, arr, N)    # 计算基于总人口的感染概率
        arr = infect(arr, beta1)           # 处理感染
        lst_inf.append(np.sum(arr == 1))   # 记录当前感染数
    
    plt.plot(x, lst_inf, label=f'{int(vac_percent*100)}%')

# 图表标注
plt.xlabel('Time')
plt.ylabel('Infected')
plt.title('SIR Model with Vaccination (β=0.3, γ=0.05)')
plt.legend(title='Vaccination Rate')
plt.show()