#WAP that inputs two tuples and print "true" if all the elements of tuple 1 is in t2.

t1 = (1, 2, 34, 54, 65, 43)
t2 = (1, 2, 34, 54, 6, 43)
count = 0
for i in t1:
    for j in t2:
        if i == j:
            count += 1

if(count == len(t1)):
    print("True")
else:
    print("False")