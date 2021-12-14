#enter a list containing number btw 1 - 12 then replace all the entries that are greater than 10 and with 10 

l1 = eval(input("Enter any number btw 1 - 12: "))
print(l1)

for i in range(len(l1)):
    if l1[i] >= 10:
        l1[i]=10
print(l1)