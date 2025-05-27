import matplotlib.pyplot as plt

'''
pseudocode

Define the bubble sort function bubble_sort for list A and B:
Swap the elements at positions in list A and list B in descending order

Define the output function output lists A and B as parameters:
Print the formatted string containing the elements in list A and B

Initialize two empty lists, provinces and populations
->
If the user input is not empty: Divide the input data by '/' and store it as a DATA list. Then add data to the lists
Otherwise: Exit the loop
->
Bubble_sort and output
->
Draw a pie chart
'''

def bubble_sort(A,B):
    n = len(A)
    for i in range(n):
        for j in range(0, n - i - 1):
            if A[j] < A[j + 1]:  
                A[j], A[j + 1] = A[j + 1], A[j]
                B[j], B[j + 1] = B[j + 1], B[j]

def output(A,B):
    print('Output the population of provinces/regions in descending order:')
    for i in range(len(A)):
        print('Population of %s: %d'%(A[i],B[i]))

provinces = []
populations = []
print('Please separate each set of data with a newline')
while True :
    raw = input('Please input the data here( Province/Population  e.g. Zhejiang/14)')
    if raw :
        data = raw.split('/')
        provinces.append(data[0])
        populations.append(int(data[1]))
    else :
        break
bubble_sort(populations,provinces)
output(provinces,populations)
plt.pie(populations, labels=provinces, autopct='%1.1f%%')
plt.title('Population of Each Regions')
plt.legend()
plt.show()