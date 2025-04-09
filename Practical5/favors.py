import pandas as pd
import matplotlib.pyplot as plt
dic = {'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5} 
print(dic)
df = pd.DataFrame(list(dic.items()), columns=['Language', 'Percentage']) #Use dataframe to draw the plot
dfsort = df.sort_values(by='Percentage',ascending=False)
#dfsort.plot.bar(x='Language', y='Percentage')
#plt.show()
#df1 = df[df.Language == 'Python']
#df2 = df[df.Language == 'SQL']
#df3 = df[df['Percentage'] >= 50]
#print(df)
#Test Codes
plt.figure(figsize=(8, 5)) 
x = df.Language
y = df.Percentage
plt.bar(x,y)
plt.legend()
plt.show() #Draw the plot

while True :
    search = input('Input the Language you want to search:')
    if search in dic:
        out = dic[search]
        break
    else :
        print('This language doesn’t exist in the dic. Please input the right language')
print(out)
