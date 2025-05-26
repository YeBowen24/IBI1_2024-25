#create dalys.py

#inport the necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read the file "Practical10" by using the absolute path 
os.chdir("D:\\Vscodefile\\IBI1_2024-25\\Practical10") #not needed in github
#os.getcwd() #test code

#read the content of the .csv file into a dataframe object 'dalys_data'
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#The code below are from the Practical and are used for testing (now they wouldn't be run)
'''
pseudo-code:
Import necessary libraries
Import os for file path operations
Import pandas for data processing and analysis
Import matplotlib.pyplot for data visualization
Import numpy for numerical computation

Set working directory and read data file
Read the CSV file "dalys-rate-from-all-causes.csv" into a DataFrame object named dalys_data

Print the first five rows of data
Access and print the data at the first row, fourth column
Access and print the data from the third row, first to fourth columns
Use iloc to access all columns for the first two rows
Use iloc to access rows 0 to 9 (every other row) and the first four columns of data
Use iloc to access columns 0, 1, 3 for the first three rows
Use iloc and a boolean list to access specific columns for the first three rows
Use loc to access "Year" column data for the third to fourth rows
Print the mean of the 'DALYs' column from the descriptive statistics

Extract and display the first 10 rows of data for Afghanistan
Use iloc to extract the first 10 rows of dalys_data and assign them to AFG
Print the third column (year column) of AFG
Print the DALYs data for the 10th row (index 9) of AFG, with a comment explaining that this is Afghanistan's 10th year DALYs data

Print the prompt "In 1990, the DALYs for all countries are shown below:"
Use boolean indexing to filter dalys_data for rows where the Year column equals 1990, and select the Entity and DALYs columns for printing

Calculate the average DALYs for each country and compare UK and France
Use groupby to calculate the average of the DALYs column in dalys_data by Entity, store the result in allmean
Get the average value for "United Kingdom" from allmean and assign it to ukmean
Get the average value for "France" from allmean and assign it to frmean
Print the average DALYs values for the UK and France, rounded to two decimal places
Compare ukmean and frmean, and set the variable comp to 'BIGGER' or 'SMALLER' based on the comparison result
Print the comparison result, stating whether the UK's average DALYs is 'bigger' or 'smaller' than France's

Plot the trend of DALYs change for the UK
Filter dalys_data for rows where the Entity column equals "United Kingdom", select the DALYs and Year columns and assign them to daly_uk
Create a new figure, plot the relationship between daly_uk.Year and daly_uk.DALYs, using blue plus markers for data points
Rotate x-axis tick labels by 60 degrees (counter-clockwise)
Set x-axis label to "Years"
Set y-axis label to "DALYs"
Set the plot title to "The DALY change of United Kingdom"
Display the plot

Plot the DALYs change trend for five countries
Open and read the first line of the file "question.txt", assign it to Qz
Print Qz
Define a list of five countries (China, France, UK, Russia, WHO region of the Americas) named Countries
Loop through each country in Countries:
    Filter dalys_data for rows where the Entity column equals the current country, select the DALYs and Year columns and assign them to dalys_i
    Plot the relationship between dalys_i.Year and dalys_i.DALYs, adding a legend label for each country
Rotate x-axis tick labels by 60 degrees (counter-clockwise)
Set x-axis label to "Years"
Set y-axis label to "DALYs"
Set the plot title to "The DALYs' change of five permanent members of the UN Security Council"
Add a legend
Display the plot
'''

# These codes are used for testing
#print(dalys_data.head(5))  #test code
#print(dalys_data.iloc[0,3]) #test code
#print(dalys_data.iloc[2,0:5]) #if the number in the position of '5' of '0:5' is bigger than the count of columns, then it would output all the columns
#print(dalys_data.iloc[0:2,:])
#print(dalys_data.iloc[0:10:2,0:5])
#dalys_data.iloc[0:3,[0,1,3]]
#my_columns = [True, True, False, True]
#dalys_data.iloc[0:3,my_columns]
#print(dalys_data.loc[2:4,"Year"])
#print(dalys_data.describe().loc['mean','DALYs'])


AFG = dalys_data.iloc[:10,:]
print(AFG.iloc[:,2]) #showing the third column (the 'Year' column) for the first 10 rows
print('The 10th year of Afghanistan DALYs data is %f'%(AFG.iloc[9,3])) #the comment of the 10th year with DALYs data recorded in AFG

print()#split the outputs

print('In 1990, the DALYs for all countries are shown below:')
print(dalys_data.loc[dalys_data.Year == 1990,['Entity','DALYs']]) #Used Boolean to show DALYs for all countries in 1990

print()#split the outputs

allmean = dalys_data.groupby('Entity').DALYs.mean() #here,'Entity' has become the index of the dataframe and could be directly used 
#print(allmean) #test code
ukmean = allmean.loc["United Kingdom"] #use the index to get the value directly
frmean = allmean.loc["France"] #the same
print('The average DALY of United Kingdom is %.2f'%(ukmean))
print('The average DALY of France is %.2f'%(frmean))
if ukmean > frmean:
    comp = 'BIGGER'
else :
    comp = 'SMALLER'
print('The UK’s average DALY is %s than the France’s'%(comp))

print()#split the outputs

#sssss

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

