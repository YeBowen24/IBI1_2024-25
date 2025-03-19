#输入：一串RNA链，三个碱基为一个蛋白质
import pandas as pd
import matplotlib.pyplot as plt
def rename(RNA):#将mRNA链转换为只有数字的列表，方便之后判定氨基酸类型
    dic={'A':0,'C':1,'G':2,'U':3}
    finRNA=[]
    for i in range(len(RNA)):
        finRNA.append(dic[RNA[i]])
    return finRNA

#正在考虑是否通过多个自定义函数来简化代码主体（就是变好看点）

amino=[[['lys','asn','lys','asn'],['thr','thr','thr','thr'],['arg','ser','arg','ser'],['ile','ile','met','ile']],[['gln','his','gln','his'],['pro','pro','pro','pro'],['arg','arg','arg','arg'],['leu','leu','leu','leu']],[['glu','asp','glu','asp'],['ala','ala','ala','ala'],['gly','gly','gly','gly'],['val','val','val','val']],[['stp','tyr','stp','tyr'],['ser','ser','ser','ser'],['stp','cys','trp','cys'],['leu','phe','leu','phe']]]
#手动建造氨基酸表，如'AAU'经过rename()之后变为'114'并通过amino[1][1][4]定位为'asn'
RNA=input('input RNA here')#输入RNA序列
'''for i in range(4):
    for j in range(4):
        print(amino[i][j])'''#检验amino acids列表有无问题
ls=rename(RNA)#转换mRNA链
#print(ls)#测试用代码
i=0
st=[]#列出全部可能的蛋白质的起点
allpt=[]#所有蛋白质的链
ptleng=[]#所以蛋白质的链长
while i <= len(ls)-3 :#开始遍历
    if ls[i] == 0 :  #寻找起始点，先找A更快
        if ls[i+1] == 3 and ls[i+2] == 2:
            st.append(i)#在起点列表中加入起点的索引
            pt={};l=0#初始化变量，pt记录氨基酸类型与数量，l记录长度
            while i <= len(ls)-3 : #注意越界，搜到倒数第三个碱基即可
                ac=amino[ls[i]][ls[i+1]][ls[i+2]]#判断密码子对应的氨基酸类型
                if ac == 'stp':#若为停止密码子，退出循环
                    break
                if ac not in pt :#若该氨基酸不在pt中，则新建键值对
                    pt[ac]=1
                else :#在pt中，值+1
                    pt[ac]+=1
                l+=1#长度+1
                i+=3#下一个密码子
            allpt.append(pt)#将此次搜索出的多肽统计加入allpt列表中
            ptleng.append(l)#存储对应的多肽长度
    i+=1#不是起始点，下一个
#print(allpt,st,ptleng)#测试用代码
# 找出最大值的索引
maxprotein = allpt[ptleng.index(max(ptleng))]#找到链最长的多肽
#print(f"最大值是: {maxprotein}")#测试用代码
df = pd.DataFrame(list(maxprotein.items()), columns=['Protein', 'Times'])#为链最长的多肽制作dataframe用于统计
df1=df.sort_values(by='Times',ascending=False)#根据氨基酸出现频率降序排列
#print(df1)#测试用代码
df1.plot.bar(x='Protein',y='Times')#绘制柱形图
plt.show()#显示柱形图
#robert.young@ed.ac.uk 课程组织者邮箱，有事发邮件