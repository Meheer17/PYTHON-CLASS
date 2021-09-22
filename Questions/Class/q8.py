# WAP to find the factorial of the Number. 5!=5*4*3*2*1 =  120

num = int(input("Enter a number: "))
n = 1
while num > 0:
        n*= num
        num -= 1
print(f"The factorial is: {n}")        