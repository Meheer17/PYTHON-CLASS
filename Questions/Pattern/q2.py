
a = int(input("Enter the no. of rows: "))
b = input("Enter the symbol: ")
print()

k=1 
n=1
for i in range(1,a+1):
        for j in range(1,k+1):
                print(end=" ")
        k += 1
        while n <= (2*(a+1-i))-1:
                print(b, end="")
                n +=1
        n=1 
        print()    