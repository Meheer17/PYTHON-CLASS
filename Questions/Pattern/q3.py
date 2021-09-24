#abc series 


n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    A = 65
    for j in range(1, i+1):
        print("%c" %(A), end="")
        A += 1
    print()