#WAP to enter any number and check it is armstrong or not

a = int(input("Enter the number: "))

sum = 0

temp = a
while temp > 0:
        digit = temp % 10
        sum += digit**3
        temp //= 10

if sum == a:
        print(a," is an amstrong number")
else: 
        print(a," is not an amstrong number")        