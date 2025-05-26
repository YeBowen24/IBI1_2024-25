import re 

def search_tata(seq): # Function to search for TATABOX
    tata = r"TATA[AT]A[AT]"
    match = re.findall(tata,seq) # Regular expression search
    if match :
        return True
    else :
        return False

def output(seq,gene):
    with open('tata_genes.fa', 'w') as file:
        for i in range(len(seq)-1):
            gene_input = '>' + gene[i] + '\n'
            seq_input = seq[i] + '\n'
            file.write(gene_input)
            file.write(seq_input)
        gene_input = '>' + gene[-1] + '\n'
        seq_input = seq[-1]
        file.write(gene_input)
        file.write(seq_input)
        file.close()

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r') as file:
    all_lines = file #read the files
    allgene = []
    geneseq = ''
    allseq = []
    for lines in all_lines :
        lines = lines.rstrip()
        if lines[0] == '>' : #deal with the gene name
            if geneseq != '' and search_tata(geneseq) :
                allgene.append(gene_name)
                allseq.append(geneseq)
            pos = lines.find('gene:') #find the gene name
            pos += 5
            gene_name = ''
            while True :
                if lines[pos] != ' ' :
                    gene_name += lines[pos]
                else :
                    break
                pos+=1
            geneseq = ''
        else : #RNA line
            geneseq = geneseq + lines
    if geneseq != '' : #Process the unprocessed sequence from the last line
        if search_tata(geneseq): #Search for tatabox
            allgene.append(gene_name)
            allseq.append(geneseq)
    file.close()
output(allseq,allgene)
print(file)