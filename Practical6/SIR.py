import numpy as np
import matplotlib.pyplot as plt
import random as r
def infect(n,beta1) :
    global beta , gamma
    if n == 0 :
        plus = np.random.choice(range(2),1,p=[1-beta1,beta1])[0]
        return n + plus
    elif n == 1 :
        plus = np.random.choice(range(2),1,p=[0.95,0.05])[0]
        return n + plus
    else :
        return n
    
def betacount():
    global beta
    num = lst.count(1)
    beta1 = beta*(num/N)
    return beta1

def count() :
    sus , inf , rec = 0 , 0 , 0
    for i in lst :
        if i == 0 : #is still sus
            sus += 1
        elif i == 1 : #is infected
            inf += 1
        else : #is recovered
            rec += 1
    ls_sus.append(sus)
    ls_inf.append(inf)
    ls_rec.append(rec)

N = 10000
time = int(input()) #input the time points
beta = 0.3 ; gamma = 0.05 #Save the probability 
lst = [0]*N #Save the status of each person
ls_sus , ls_inf , ls_rec = [N-1] , [1] , [0] #Save the numbers of each kind of people
lst[-1] = 1 #The first person's status is changed to '1'(infected)
for i in range(time): #loop
    beta1=betacount()
    for j in range(len(lst)) :
        lst[j]=infect(lst[j],beta1) #change the status of each person
    count() #record the status
x = list(range(time+1))
plt.figure(figsize=(6,4),dpi=150)
plt.plot(x, ls_sus, label='suspected', color='b')
plt.plot(x, ls_inf, label='infected', color='g')
plt.plot(x, ls_rec, label='recovered', color='r')
plt.show()
#print(max(ls_inf))