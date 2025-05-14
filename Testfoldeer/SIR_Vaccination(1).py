'''
#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#Define population
N = 10000
#Define initial infected population
I = 1
#Define initial susceptible population
S = N - I
#Define initial recovered population
R = 0  
#Define initial infection rate
beta = 0.3
#Define recovery rate
gamma = 0.05

# Define the vaccination rate (fraction of susceptible population vaccinated per time step)
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 ]  # 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, and 100% vaccination rates
# Create a plot for each vaccination rate
plt.figure(figsize=(8, 6), dpi=150)

S_array = [S] 
I_array = [I]   
R_array = [R]

# Run the SIR model for each vaccination rate
for vaccination_rate in vaccination_rates:
    for t in range(1000):
        # calculate number of infected individuals
        I = I + beta * S * I / N
        # calculate number of recovered individuals
        R = R + gamma * I
        # calculate number of susceptible individuals  
        S = S - beta * S * I / N - gamma * I - vaccination_rate * S
        
    # append values to arrays
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)
# Plot the SIR model for this vaccination rate
plt.plot(I_array, label=f'Vaccination Rate = {vaccination_rates*100}%')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.title('SIR Model with Different Vaccination Rates')
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt

# ----------------------
# 参数设置
# ----------------------
N = 10000          # 总人口
beta = 0.3         # 感染率
gamma = 0.05       # 康复率
time_steps = 1000  # 模拟时间步数
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  # 疫苗接种率

plt.figure(figsize=(8, 6), dpi=150)

# ----------------------
# 修正逻辑
# ----------------------
for vaccination_rate in vaccination_rates:
    # 初始化状态（确保 S 非负）
    V = int(N * vaccination_rate)
    S = max(N - 1 - V, 0)  # 关键修正1：强制 S ≥ 0
    I = 1 if S >= 0 else 0  # 关键修正2：如果 S < 0，初始感染者为0
    R = 0
    
    I_values = [I]  # 记录感染人数
    
    for t in range(time_steps):
        # ----------------------
        # 感染者康复
        # ----------------------
        new_R = np.random.binomial(I, gamma) if I > 0 else 0
        I -= new_R
        R += new_R
        
        # ----------------------
        # 易感者被感染
        # ----------------------
        if S > 0:  # 关键修正3：仅当 S > 0 时计算感染
            infection_prob = beta * I / N
            new_I = np.random.binomial(S, infection_prob)
            new_I = min(new_I, S)  # 关键修正4：确保感染人数不超过剩余易感者
            S -= new_I
            I += new_I
        else:
            new_I = 0  # 无易感者时跳过感染
        
        I_values.append(I)
    
    #plt.plot(range(time_steps+1), I_values, label=f'{int(vac_rate*100)}%')

# ----------------------
# 绘图
# ----------------------
plt.xlabel('Time')
plt.ylabel('Infected Population')
plt.title('Stochastic SIR Model with Vaccination')
plt.legend(title='Vaccination Rate')
plt.show()