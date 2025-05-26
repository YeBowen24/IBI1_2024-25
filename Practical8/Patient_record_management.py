class Patients:
    def __init__(self,info):
        self.name = info[0]
        self.age = int(info[1])
        self.recent = info[2]
        self.history = info[3]

    def printall(self):
        print(f'Name:{self.name} ; Age:{self.age} ; Latest submission(yyyy/mm/dd):{self.recent} ; Medical History:{self.history}')
    
p_name = input('Input your name here: ')
p_age = input('Input your age here: ')
p_recent = input('Input the date of latest admission here(yyyy/mm/dd): ')
p_history = input('Input your medical history: ')
'''
input your personal information here

e.g. My name is John Smith. I'm 41 years old. My latest admission is 2014.3.31. My medical history is Heart Attack.
Then I need to input all the information in sequence in the terminal with the guidance (like the ones below).
Input your name here: John Smith
Input your age here: 41
Input the date of latest admission here(yyyy/mm/dd): 2014/3/31
Input your medical history: Heart Attack
'''
info = [p_name,p_age,p_recent,p_history]
patient1 = Patients(info)
patient1.printall()