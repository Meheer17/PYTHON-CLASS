#write a menu driven program 1.UPPERCASE 2.lowercase 3.digits 4.special program 5.end option

str1 = input("Enter your string: ")

print()
print('''1. Find the no. of uppercase in the string
2. Find the no. of lowercase
3. The no. of digits in the string
4. The no. of special characters
5. End''')

print()
op = int(input("Enter the option: "))

print()

if op == 1:
        c = 0
        for i in str1:
                i1 = ord(i)
                if  i1 >= 60 and i1 <= 90:
                        c += 1 
        print("The no. of uppercase is ",c)
elif op == 2:
        c = 0
        for i in str1:
                i1 = ord(i)
                if  i1 >= 97 and i1 <= 122:
                        c += 1 
        print("The no. of lowercase is ",c)  
elif op == 3:
        c = 0
        for i in str1:
                if i.isdigit():
                        c += 1
        print("The no. of digits is ",c)
elif op == 4:
        c = 0
        for i in str1:
                if not(i.isalnum()):
                        c += 1
        print("The no. of special charater is ",c) 
else:
        print("***---END---***")
