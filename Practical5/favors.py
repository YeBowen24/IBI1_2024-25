import pandas as pd
import matplotlib.pyplot as plt
dic = {'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}
df = pd.DataFrame(list(dic.items()), columns=['Language', 'Percentage'])
dfsort = df.sort_values(by='Percentage',ascending=False)
#dfsort.plot.bar(x='Language', y='Percentage')
#plt.show()
#df1 = df[df.Language == 'Python']
#df2 = df[df.Language == 'SQL']
#df3 = df[df['Percentage'] >= 50]
print(df)
search = input()
out = df[df.Language == search]['Percentage']
print(out)
