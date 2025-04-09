class Patients:
    def __init__(self,info):
        self.name = info[0]
        self.age = int(info[1])
        self.recent = info[2]
        self.history = info[3]

    def printall(self):
        print(f'Name:{self.name} ; Age:{self.age} ; Latest submission(yyyy/mm/dd):{self.recent} ; Medical History:{self.history}')
    
p_name = input('input your name here:')
p_age = input('input your age here:')
p_recent = input('input the date of latest admission here(yyyy/mm/dd):')
p_history = input('input your medical history:')
'''
input your personal information here(e.g. My name is John Smith. I'm 41 years old. My latest admission is 2014.2.2. My medical history is Heart Attack, then I need to input all the information with the guidance )
'''
info = [p_name,p_age,p_recent,p_history]
patient1 = Patients(info)
patient1.printall()