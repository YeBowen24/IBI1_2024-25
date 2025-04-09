import matplotlib.pyplot as plt

provinces = []
populations = []
print('Please separate each set of data with a newline')
while True :
    raw = input('Please input the data here( Province/Population  e.g. Zhejiang/14)')
    if raw :
        data = raw.split('/')
        provinces.append(data[0])
        populations.append(data[1])
    else :
        break
plt.pie(populations, labels=provinces)
plt.legend()
plt.show()