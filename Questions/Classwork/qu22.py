#Write a program to remove all the duplicates from a list and store it in a tuple.

s = eval(input("Enter ur list: "))
l1 =[]
for i in s:
    if i not in l1:
        l1.append(i)
t1 = tuple(l1)
print(t1) 