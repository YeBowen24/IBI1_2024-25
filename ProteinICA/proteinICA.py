#输入：一串RNA链，三个碱基为一个蛋白质
#先定义一个三维蛋白质库
import pandas as pd
import matplotlib.pyplot as plt
def rename(RNA):
    dic={'A':0,'C':1,'G':2,'U':3}
    finRNA=[]
    for i in range(len(RNA)):
        finRNA.append(dic[RNA[i]])
    return finRNA

amino=[[['lys','asn','lys','asn'],['thr','thr','thr','thr'],['arg','ser','arg','ser'],['ile','ile','met','ile']],[['gln','his','gln','his'],['pro','pro','pro','pro'],['arg','arg','arg','arg'],['leu','leu','leu','leu']],[['glu','asp','glu','asp'],['ala','ala','ala','ala'],['gly','gly','gly','gly'],['val','val','val','val']],[['stp','tyr','stp','tyr'],['ser','ser','ser','ser'],['stp','cys','trp','cys'],['leu','phe','leu','phe']]]
RNA=input('input RNA here')#输入RNA序列
'''for i in range(4):
    for j in range(4):
        print(amino[i][j])'''#检验amino acids有无问题
ls=rename(RNA)
#print(ls)
i=0
st=[]
allpt=[]
ptleng=[]
while i <= len(ls)-3 :#开始遍历
    if ls[i] == 0 :  #寻找起始点
        if ls[i+1] == 3 and ls[i+2] == 2:
            st.append(i)
            pt={};l=0
            while i <= len(ls)-3 : #注意越界
                ac=amino[ls[i]][ls[i+1]][ls[i+2]]
                if ac == 'stp':
                    break
                if ac not in pt :
                    pt[ac]=1
                else :
                    pt[ac]+=1
                l+=1
                i+=3
            allpt.append(pt)
            ptleng.append(l)
    i+=1
print(allpt,st,ptleng)
# 找出最大值的索引
maxprotein = allpt[ptleng.index(max(ptleng))]

#print(f"最大值是: {maxprotein}")
df = pd.DataFrame(list(maxprotein.items()), columns=['Protein', 'Times'])
df1=df.sort_values(by='Times',ascending=False)
#print(df1)
#待接入绘图模块
df1.plot.bar(x='Protein',y='Times')
plt.show()
#robert.young@ed.ac.uk