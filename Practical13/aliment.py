

def distance_count(seq1,seq2):
    edit_distance = 0 #set initial distance as zero
    for i in range(len(seq1)): #compare each amino acid
        if seq1[i]!=seq2[i]:
            edit_distance += 1 #add a score 1 if amino acids are different
    return edit_distance

def read_seq(file_name):
    with open('%s'%(file_name), 'r') as file:
        geneseq = ''#临时存储基因序列用的变量
        for lines in file:
            lines = lines.rstrip() #去除换行符
            if lines[0] == '>' : #deal with the gene name
                continue
            else : #RNA 序列存储
                geneseq = geneseq + lines
        file.close()
    return geneseq

mouse_gene = 'P09671.fa'
human_gene = 'P04179.fa'
mouse_seq = read_seq(mouse_gene)
human_seq = read_seq(human_gene)
edit_distance = distance_count(mouse_seq,human_seq)
print(round(edit_distance/222,2))
rnd_gene = 'random_222.fa'
rnd_seq = read_seq(rnd_gene)
edit_mouse_rand = distance_count(mouse_seq,rnd_seq)
print(round(edit_mouse_rand/222,2))
edit_human_rand = distance_count(human_seq,rnd_seq)
print(round(edit_human_rand/222,2))