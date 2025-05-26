'''
import re
#The code can use re library to easily search the string, but this is not necessary. So I abandoned this code
def find_s(seq,s): 
    lst = []
    matches = re.finditer(seq, s)
    for match in matches:
        lst.append(match.start())
    return lst
'''
seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA' # you can change the sequence here
beg = 'GT'
end = 'AG'
begin = -1
ending = len(seq) 
for i in range(len(seq)-1):
    if seq[i:i+2] == beg :
        begin = i
        break
for j in range(len(seq)-1,0,-1):
    if seq[j-1:j+1] == end :
        ending = j
        break
maxlen = ending-begin+1
if begin == -1 or ending == len(seq) :
    print('The intron that meets the conditions does not exist.')
if maxlen >=4:
    print('The length of the largest possible intron is %d'%(maxlen))