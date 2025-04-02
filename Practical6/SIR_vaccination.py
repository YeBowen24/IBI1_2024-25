import numpy as np
import matplotlib.pyplot as plt
import random as r
def infect(array,beta1) :
    N = 10000
    plus = np.array(np.random.choice(range(2),len(array),p=[1-beta1,beta1]))
    array = array + plus
    for i in range(len(array)) :
        if array[i] >= 2:
            array[i] = 2
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
time = int(input("input loop time here"))
x = list(range(time+1))
N = 10000
beta = 0.3 ; gamma = 0.05 #Save the probability 
for vac in range(0,101,10):
    vac=round(vac/100,2)
    vac_n =int(vac * N)
    lst = [0]*(N-vac_n) #Save the status of each person
    arr = np.array(lst) #Change the data form to array
    lst_inf = [0]
    if vac != 1:
        arr[-1] = 1 #The first person's status is changed to '1'(infected)
        lst_inf=[1]
    for i in range(time): #loop
        beta1=betacount(beta,arr)
        arr=infect(arr,beta1) #change the status of each person
        inf_num=count(arr) #record the status
        lst_inf.append(inf_num)
    plt.plot(x, lst_inf, label=str(int(vac*100))+'%' )
plt.legend()
plt.show()
