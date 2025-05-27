'''
pseudocode
Prompt the user to input the weight (unit: kilograms), and convert it to an integer to store in the variable "weight"
Prompt the user to enter the height (unit: meters), and convert it to a floating-point number to store in the variable "height"
To calculate the BMI value, the formula is: BMI = weight/(height)^2, and keep the result to two decimal places
Print the BMI value of the user in the format of "Your BMI is followed by the calculated BMI value".
'''

weight = int(input('input your weight here(kg)'))
height = float(input('input your height here(m)'))
BMI = round(weight/height**2,2)
print("Your BMI is",BMI)
