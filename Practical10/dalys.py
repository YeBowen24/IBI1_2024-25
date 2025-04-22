import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("D:\\Vscodefile\\IBI1_2024-25\\Practical10")
#os.getcwd() #test code
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#print(dalys_data.head(5))  #test code
#print(dalys_data.iloc[0,3]) #test code
#print(dalys_data.iloc[2,0:5])
#print(dalys_data.iloc[0:2,:])
#print(dalys_data.iloc[0:10:2,0:5])
#dalys_data.iloc[0:3,[0,1,3]]
#my_columns = [True, True, False, True]
#dalys_data.iloc[0:3,my_columns]
#print(dalys_data.loc[2:4,"Year"])

#The code above are from the Practical and are used for testing

AFG = dalys_data.iloc[:10,:]
print(AFG.iloc[:,2]) #showing the third column (the 'Year' column) for the first 10 rows
print('The 10th year of Afghanistan DALYs data is %f'%(AFG.iloc[9,3])) #the comment of the 10th year with DALYs data recorded in AFG

print()#split the outputs

print('In 1990, the DALYs for all countries are shown below:')
print(dalys_data.loc[dalys_data.Year == 1990,['Entity','DALYs']])

print()#split the outputs

allmean = dalys_data.groupby('Entity').DALYs.mean() #here,'Entity' has become the index of the dataframe and could be directly used 
#print(allmean) #test code
ukmean = allmean.loc["United Kingdom"] #use the index to get the value directly
frmean = allmean.loc["France"] #the same
if ukmean > frmean:
    comp = 'BIGGER'
else :
    comp = 'SMALLER'
print('The UK’s average DALY is %s than the France’s'%(comp))

print()#split the outputs

daly_uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]] #get the 'Year' and 'DALYs' column and data
plt.plot(daly_uk.Year, daly_uk.DALYs, 'b+') #'b+'string : color and the type of the each data point(here I use the default value)
plt.xticks(daly_uk.Year,rotation=60) #Asked AI for this code: rotation: Positive numbers represent counterclockwise rotation of the X-axis label, and negative numbers represent clockwise rotation of the label
plt.xlabel("Years") #This may be UNVISIBLE because of the rotation of the xticks
plt.ylabel("DALYs")
plt.title('The DALY change of United Kingdom')
plt.show()

print()#split the outputs

with open("question.txt", "r", encoding="utf-8") as ques:
    Qz = ques.readline() #the question is in the first line of the file
    print(Qz) #print the question
    Countries = ['China','France','United Kingdom','Russia','Region of the Americas (WHO)'] #the list of five permanent members of the UN Security Council
    for count in Countries:
        dalys_i = dalys_data.loc[dalys_data.Entity == count, ["DALYs", "Year"]]
        plt.plot(dalys_i.Year, dalys_i.DALYs,label = count) #default plot
    plt.xticks(dalys_i.Year,rotation=60) #Asked AI for this code: rotation: Positive numbers represent counterclockwise rotation of the X-axis label, and negative numbers represent clockwise rotation of the label
    plt.xlabel("Years") #This may be UNVISIBLE because of the rotation of the xticks
    plt.ylabel("DALYs")
    plt.title("The DALYs' change of five permanent members of the UN Security Council")
    plt.legend()
    plt.show()



