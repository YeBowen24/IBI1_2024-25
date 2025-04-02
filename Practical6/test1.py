import matplotlib.pyplot as plt
import numpy as np
N = 10
beta1 = 0.4
plus = np.random.choice(range(2),N,p=[1-beta1,beta1])
print(plus)