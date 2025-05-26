import numpy as np
import matplotlib.pyplot as plt
import random as r

def status(array,beta1) : 
    global gamma
    # Asked AI and used AI-generated code
    operation = {0: lambda x: x + np.random.choice([0, 1], p=[1 - beta1, beta1]), 1: lambda x: x + np.random.choice([0, 1], p=[1 - gamma, gamma]), 2: lambda x: x}
    array = np.array([operation[status](status) for status in array])
    return array
    
def betacount(beta,array):
    N = 10000
    num = list(array).count(1)
    beta1 = beta*(num/N)
    return beta1

def count(array) :
    inf = list(array).count(1)
    return inf

plt.figure(figsize=(6,4),dpi=150)
time = int(input("input loop time here: "))
x = list(range(time+1))
N = 10000
beta = 0.3 ; gamma = 0.05 #Save the probability 
for vac in range(0,101,10):
    vac=round(vac/100,2)
    vac_n =int(vac * N) #A fraction of the population is vaccinated
    lst = [0]*(N-vac_n) #only calc the people who aren't vaccinated to decrease the calculation 
    arr = np.array(lst) #Change the data form to array
    lst_inf = [0]
    if vac_n != N:
        arr[-1] = 1 #The first person's status is changed to '1'(infected)
        lst_inf=[1]
    for i in range(time): #loop
        beta1=betacount(beta,arr)
        arr=status(arr,beta1) #change the status of each person
        inf_num=count(arr) #record the status
        lst_inf.append(inf_num)
    plt.plot(x, lst_inf, label=str(int(vac*100))+'%' )
plt.xlabel('Time')
plt.ylabel('Person Count')
plt.legend()
plt.show()
