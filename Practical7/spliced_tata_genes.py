import re 

def search_tata(seq): #Function that search the tata structure
    tata = r"TATA[AT]A[AT]"
    match = re.findall(tata,seq) #regular expression search, 'match' is list
    if match :
        return True
    else :
        return False

def count_tata(seq): #count the number of tata structure
    tata = r"TATA[AT]A[AT]"
    all_tata = re.findall(tata,seq)
    return len(all_tata)

def output(seq,gene,file_name): #create and write the file
    with open('%s'%(file_name), 'w') as file:
        for i in range(len(seq)-1):
            file.write(gene[i]+'\n')
            file.write(seq[i]+'\n')
        file.write(gene[-1]+'\n')  #Slightly increases the storage space used by the code, but slightly reduces the running time.
        file.write(seq[-1])
        file.close()

def judge_in(sp, seq):
    global gene_name
    beg = sp[:2]
    end = sp[2:]
    begin = seq.find(beg) #search the beginning
    if begin != -1:
        ending = seq.find(end,begin) #just search the first beg and the last end
    else :
        ending = -1
    if ending != -1 :
        count = count_tata(geneseq) #This is the count of TATAbox structure
        output_line = '>%s -- %d TATAbox(es) in its structure.'%(gene_name,count)
        allgene.append(output_line) #add the gene name and the count of tata
        allseq.append(geneseq) #add the sequence along with the gene name

all_sp = ['GTAG', 'GCAG','ATAC']
while True : #Check the input is valid or not
    sp = input('Input one of three possible splice donor/acceptor combinations (GTAG/GCAG/ATAC) here.')
    if sp in all_sp :
        break
    else :
        print('Invalid input. Please choose one of three possible splice donor/acceptor combinations (GTAG/GCAG/ATAC).')
file_name = '%s_spliced_genes.fa'%(sp)  #Create filename based on input

allseq = [] #Store all the genetic sequences
allgene = [] #Store all the genetic names
gene_name = '' #prevent the errors

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r') as file: 
    all_lines = file #read the files #Variable type: list
    geneseq = ''#Temporary variable for storing gene sequences
    for lines in all_lines :
        lines = lines.rstrip() #Remove newline characters
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
        else : #Remove newline characters
            geneseq = geneseq + lines
    if geneseq != '' and search_tata(geneseq):
        judge_in(sp, geneseq)
    file.close()
output(allseq,allgene,file_name)
print('The file has been successfully generated!')