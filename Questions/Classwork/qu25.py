#WAP for a given tuple pair find which is even.

t1 = ((1, 2), (34, 56), (4,7), (2,6), (9, 9), (56, 66), (88, 98), (56, 79), (66, 74))
y = 1
count = 0
for i in range(len(t1)):
    for j in range(len(t1[i]) - 1):
 
        if t1[i][j] % 2 == 0 and t1[i][y] % 2 == 0:
            count += 1

print(count)