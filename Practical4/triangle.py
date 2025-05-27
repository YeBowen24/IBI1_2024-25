def tri_sum(t):
    num = 0
    for i in range(1,t+1): #range(2,1)  --- []
        num += i
    print (num,end = '  ')

time = int(input('Input time loop: '))

for i in range(1,time+1):
    tri_sum(i)
