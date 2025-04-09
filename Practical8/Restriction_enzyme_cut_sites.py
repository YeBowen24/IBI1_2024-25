import re

def errfnd(seq):
    match = re.search(r"[^ACGT]", seq) #I asked AI to give me this code
    if match :
        return True
    else :
        return False

while True :
    seq = input('Input the DNA sequence HERE: ')
    fnd = input('Input the restriction digest you want to find:')
    err = errfnd(seq) and errfnd(fnd)
    if not err :
        break
    print('Illegal nucleotide, please input the sequence that only contains "ACGT"!')

place = re.search(fnd,seq)
if place :
    print('The restriction digest start at the %dth nucleotide.'%(place.start()))
else :
    print('The sequence you want to search is not in the DNA sequence!')

'''
Here are some examples:
seq1 = 'UGCGAUGAAGAGUUCCGACU'
seq2 = 'TTCTTATAGTATCGTACCTGGTGAGCCCCG'
fnd0 = 'UAAU'
fnd1 = 'AGTTTT'
fnd2 = 'TCGTA'
if you input seq1 or fnd0, then the code will output 'Illegal nucleotide, please input the sequence that only contains "ACGT"!'
if you input seq2 and fnd1, then the code will output 'The sequence you want to search is not in the DNA sequence!'
if you input seq2 and fnd2, then the code will output 'The restriction digest start at the 11th nucleotide.'
'''