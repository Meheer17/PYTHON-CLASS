#WAP to get random int and then sort it as even and odd

import random
e = []
o = []
l1=[]
for i in range(11):
    l1.append(random.randint(0,100))

for j in l1:
    if j % 2 == 0:
        e.append(j)
    else:
        o.append(j)

print(f"The random list is {l1}")
print(f"The even numbers are {e}")
print(f"The odd numbers are {o}")