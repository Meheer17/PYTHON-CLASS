#WAP to enter Lower_limit, Upper_Limit and find the sum of all odds and evens number between the range separately

a = int(input('Enter the Lower Limit of the range: '))
b = int(input('Enter the Upper Limit of the range: '))

evenSum = 0
oddSum = 0

for c in range(a,b+1):
        if c % 2 == 0:
                evenSum = evenSum + c
        else:
                oddSum = oddSum + c        

print('The sum of the even numbers in your range {} to {} is equal to {}'.format(a,b,evenSum))
print('The sum of the odd numbers in your range {} to {} is equal to {}'.format(a,b,oddSum))