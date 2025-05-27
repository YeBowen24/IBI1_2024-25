import pandas as pd
import matplotlib.pyplot as plt

'''
pseudocode

Create a dictionary with programming languages as keys and their corresponding percentages as values, then print the dictionary
 
Convert the dictionary to a pandas DataFrame with column names 'Language' and 'Percentage'
 
Sort the DataFrame by the 'Percentage' column in descending order
 
Plot a bar chart, set the figure size, with x-axis as 'Language' and y-axis as 'Percentage'
 
Add x-axis label as 'Language Type', y-axis label as 'Number of Users', include a legend, and finally display the chart
 
Start an infinite loop:
Prompt the user to input the programming language they want to search
If the input language exists in the dictionary:
Get the corresponding percentage and store it in variable 'out'
Break the loop
Else:
Notify the user that the language doesn't exist in the dictionary and request correct input
Print the variable 'out' (the percentage found for the user's query)
'''

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
plt.xlabel('Language Type')
plt.ylabel('Number of Users')
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
