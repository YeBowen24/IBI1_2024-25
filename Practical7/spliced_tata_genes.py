import re 

def search_tata(seq): #搜索TATABOX的函数
    tata = r"TATA[AT]A[AT]"
    match = re.findall(tata,seq)#正则表达式搜索
    if match :
        return True
    else :
        return False

def count_tata(seq): #对TATABOX结构数量进行计数
    tata = r"TATA[AT]A[AT]"
    all_tata = re.findall(tata,seq)
    return len(all_tata)

def output(seq,gene,file_name): #写入文件
    with open('D:/vscodefile/IBI1_2024-25/Practical7/%s'%(file_name), 'w') as file:
        for i in range(len(seq)-1):
            file.write(gene[i]+'\n')
            file.write(seq[i]+'\n')
        file.write(gene[-1]+'\n')  #增加代码存储空间，但是适量减少运行时间
        file.write(seq[-1])
        file.close()

def judge_in(sp, geneseq):
    global gene_name
    if sp in geneseq : #处理上一次的遗留序列
        count = count_tata(geneseq) #这是TATAbox的计数
        output_line = '>%s -- %d TATAbox(es) in its structure.'%(gene_name,count)
        allgene.append(output_line) #写入基因名称以及计数
        allseq.append(geneseq)

all_sp = ['GTAG', 'GCAG','ATAC']
while True : #判断输入是否合法
    sp = input('Input one of three possible splice donor/acceptor combinations (GTAG/GCAG/ATAC) here.')
    if sp in all_sp :
        break
    else :
        print('Invalid input. Please choose one of three possible splice donor/acceptor combinations (GTAG/GCAG/ATAC).')
file_name = '%s_spliced_genes.fa'%(sp)  #根据输入创建文件名

allseq = [] #存储所有的基因序列
allgene = [] #存储所有的基因名称
gene_name = '' #防报错

with open("D:/vscodefile/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r') as file: 
    all_lines = file #read the files #变量类型：列表
    geneseq = ''#临时存储基因序列用的变量
    for lines in all_lines :
        lines = lines.rstrip() #去除换行符
        if lines[0] == '>' : #deal with the gene name
            if geneseq != '' and search_tata(geneseq):
                judge_in(sp, geneseq)
            pos = lines.find('gene:') #find the gene name
            pos += 5
            gene_name = '' #reset gene name
            while True :
                if lines[pos] != ' ' :
                    gene_name += lines[pos]
                else :
                    break
                pos+=1
            geneseq = ''
        else : #RNA 序列存储
            geneseq = geneseq + lines
    if geneseq != '' and search_tata(geneseq):
        judge_in(sp, geneseq)
    file.close()
output(allseq,allgene,file_name)
print(file)