#WAP to enter any number and find its reverse

a = int(input('Enter your number: '))
rev = 0
while a > 0:
        rem = a % 10
        rev = (rev * 10) + rem
        a = a//10
print('Reverse of the number is: ',rev)        