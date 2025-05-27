'''
Get the input 'time' value representing the number of triangular numbers to generate

Initialize a variable to store the triangular number value

Loop from 1 to time (inclusive):
    Add the current loop index value to the triangular number storage variable
    Print the calculated current triangular number value followed by a space
'''

def tri_sum(t):
    num = 0
    for i in range(1,t+1): #range(2,1)  --- []
        num += i
    print (num,end = '  ')

time = int(input('Input time loop: '))

for i in range(1,time+1):
    tri_sum(i)
