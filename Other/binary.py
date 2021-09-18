# Enter a num for its binary Value.

num = int(input("Enter your number: "))
while num > 0:
        rem = num % 10
        rem = rem/2
        binary = str(rem)
        print(binary)