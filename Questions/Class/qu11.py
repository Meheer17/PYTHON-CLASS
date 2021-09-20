#WAP to make diamond

a = int(input("Enter the no. of rows: "))
b = input("Enter the symbol: ")
n = 0
for i in range( 1, ( a + 1)):
        for j in range(1, ( a - i ) + 1):
                print(end=" ")
        while n != ((2*i)-1):
                print(b, end="")
                n += 1
        n=0
        print()
k=1 
n=1
for i in range(1,a):
        for j in range(1,k+1):
                print(end=" ")
        k += 1
        while n <= (2*(a-i))-1:
                print(b, end="")
                n +=1
        n=1 
        print()          