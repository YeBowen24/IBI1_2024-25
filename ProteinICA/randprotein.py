#这段代码用于生成随机的测试用的mRNA序列

import random as r
length = int(input('RNA length: '))
amino = "ACGU"
RNA = ''
for i in range(length):
    pt = r.randint(0,3)
    RNA = RNA + amino[pt]
print(RNA)