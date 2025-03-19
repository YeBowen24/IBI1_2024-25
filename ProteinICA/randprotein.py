import random as r
length = int(input('RNA length: '))
amino = "ACGU"
RNA = ''
for i in range(length):
    pt = r.randint(0,3)
    RNA = RNA + amino[pt]
print(RNA)