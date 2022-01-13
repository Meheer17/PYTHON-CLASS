#wap to find the frequency in dict

s = input("Enter the string here: ")
w = s.split()
print(s)
print(w)
d = dict()
for i in w: 
    key = i
    if key not in d: 
        c = w.count(i)
        d[key] = c
print(d)