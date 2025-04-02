seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
beg = 'GT'
end = 'AG'
begin = 0
ending = len(seq)
for i in range(len(seq)-1):
    if seq[i:i+2] == beg :
        begin = i
        break
for j in range(len(seq)-1,0,-1):
    if seq[j-1:j+1] == end :
        ending = j
        break
maxlen = j-i+1
if maxlen >=4:
    print(maxlen)