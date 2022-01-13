#WAP TO count the freqency of int 
d =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
f = {}
for i in d:
    if i in f:
        f[i]+=1
    else: 
        f[i] = 1
print(f)