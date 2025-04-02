import numpy as np
import matplotlib.pyplot as plt

# ----------------------
# 参数设置
# ----------------------
GRID_SIZE = 100      # 网格尺寸 (100x100)
BETA = 0.3           # 感染概率
GAMMA = 0.05         # 康复概率
TIME_STEPS = 100     # 模拟时间步数
SAVE_TIMES = [0, 10, 50, 100]  # 需要保存图像的时间点

# ----------------------
# 初始化网格
# ----------------------
population = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)  # 0=易感者, 1=感染者, 2=康复者

# 随机选择初始感染者坐标
outbreak = np.random.choice(GRID_SIZE, size=2)
population[outbreak[0], outbreak[1]] = 1

# ----------------------
# 时间循环
# ----------------------
for t in range(TIME_STEPS + 1):
    # --- 步骤1: 处理感染者康复 ---
    # 找到所有感染者坐标 (状态1)
    infected_coords = np.argwhere(population == 1)
    
    # 生成康复随机掩码
    recovery_mask = np.random.rand(len(infected_coords)) < GAMMA
    # 将满足条件的感染者转为康复者 (状态2)
    for idx in infected_coords[recovery_mask]:
        population[tuple(idx)] = 2

    # --- 步骤2: 处理新感染 ---
    new_infections = []
    # 遍历所有当前感染者
    for (i, j) in infected_coords:
        # 检查8个邻居
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue  # 跳过自身
                ni, nj = i + di, j + dj
                # 检查边界
                if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE:
                    # 仅感染易感者 (状态0)
                    if population[ni, nj] == 0 and np.random.rand() < BETA:
                        new_infections.append((ni, nj))
    
    # 批量更新新感染者 (避免重复感染)
    for (ni, nj) in new_infections:
        if population[ni, nj] == 0:  # 二次确认状态
            population[ni, nj] = 1

    # --- 步骤3: 保存关键时间点图像 ---
    if t in SAVE_TIMES:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(
            population,
            cmap='viridis',    # 颜色映射: 0=深紫(易感), 1=蓝绿(感染), 2=黄(康复)
            interpolation='nearest'
        )
        plt.title(f'2D SIR Model (t={t})')
        plt.axis('off')
        plt.savefig(f'spatial_SIR_t{t}.png')
        #plt.close()

# ----------------------
# 输出说明
# ----------------------
print("模拟完成！已生成以下时间点热图:")
print(f"--> spatial_SIR_t{SAVE_TIMES}.png")