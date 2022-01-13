#WAP to rotate a list forward and backward

l= [1,2,3,4,5,6,7,8,9]
print("1. Rotate right by 1 \n2. Rotate left by 1 \n3. Show array")
c = int(input("Enter the choice 1-3: "))
n = len(l) 
while True: 
    if c == 1: 
        temp = l[0]
        for i in range(n-1):
            l[i] = l[i+1]
        l[n-1] = temp
        print(l)
    elif c == 2:
        temp = l[n-1]
        for i in range(n-2, -1, -1):
            l[i+1] = l[i]
        l[0] = temp
        print(l)
        
    elif c == 3: 
        for i in range(n): 
            print(l[i], end=" ")
    else: 
        break
    print()
    ch = input("Do u want to continue?? (Y/N)")
    if ch == "Y" or ch == "y":
        c = int(input("Enter the choice 1-3: "))
    else:
        break