#Wap to print the following fabiconni series...

n = int(input("Enter number of terms in the series: "))
n1, n2 = 0,1
print("Fibonacci series- ", n1,n2,end=' ')
for i in range(3, n+1):
        nn=n1+n2
        print(nn,end=',')
        n1=n2
        n2=nn