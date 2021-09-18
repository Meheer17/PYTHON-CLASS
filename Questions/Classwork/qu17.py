# find occurence of a substring a strng, use str func and without str func

str1 = input("Enter the string: ")
str2 = input("Enter the string u wanna find: ")
print()
print(''' MENU 
1. With string func
2. Without string func''')
print()
op = int(input("Enter the option: "))
print()
if op == 1:
        print(str1.count(str2))
elif op == 2:
        words = str1.split()
        c = 0
        for i in words:
                if i == str2:
                        c += 1
        print("The no. of occurence is ",c)
else:
        print("Invaild choice!!")
        