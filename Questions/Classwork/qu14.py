#WAP to enter any number and check if its palindrome number or not

a = input("Enter the number: ")

if a == a[::-1]:
        print("The number is a Palindrome Number")
else:
        print("The number is not a Palindrome Number")
print(a[::-1])
