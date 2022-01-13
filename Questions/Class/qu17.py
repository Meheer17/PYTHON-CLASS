#WAP to accept nested list and d othe follwoing: 1. add in nest list 2 delete in nested list 3 exit.


n1 = eval(input("Enter matrix 1(3*3): "))
n2 = eval(input("Enter matrix 2(3*3): "))
result = [[0,0,0],[0,0,0],[0,0,0]]
while True: 
    print(" 1. Addition of the two matrix \n 2. Subtraction of the two matrix \n 3. Exit")
    c = int(input("Enter the choice: "))
    if c == 1: 
        for i in range(len(n1)):
            for j in range(len(n1[0])):
                result[i][j]= n1[i][j] + n2[i][j]
        for r in result: 
            print(r)

    if c == 2:
        for i in range(len(n1)):
            for j in range(len(n1[0])):
                result[i][j]= n1[i][j]-n2[i][j]
        for r in result:
            print(r)
    else:
        break