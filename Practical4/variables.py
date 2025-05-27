a = 15
b = 60 + 15
c = a + b
d = 60 + 30
e = 5
f = d + e
if f > c:
    print('f is greater than c')
else: 
    print('c is greater than f')

print('IS c greater than e? ',end='')
print(c>e)

X = True ; Y = False
W = [X and Y, not X and Y, X and not Y, not X and not Y, X or Y, not X or Y, X or not Y, not X or not Y]
print(W)