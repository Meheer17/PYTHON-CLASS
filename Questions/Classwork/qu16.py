# take 2 stings concate and replicate and let the user choose which one to print

str1 = input("Enter your first sting: ")
str2 = input("Enter your second string: ")

print()
print(str1+' '+str2)
print()

print('''1.Print the first string
2.Print the first string''')

print()
c = int(input("Enter your chioce: "))         
if c==1:
        print((str1+' ')*3)
elif c==2:
        print((str2+' ')*5)
else:
        print("INVAILD CHOICE")                
        