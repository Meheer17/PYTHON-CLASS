a=["hello", 1205, 1222, "hello", 1205, 1205, 1205]
u=[]
d=[]
for i in a:
    if i not in u:
        u.append(i)
    else:
        if i not in d:
            d.append(i)
print(u)
print(d)