# creating a following list using a for loop a 1. list consititng of interger 0 through 50 2. list containg teh squares of the interger 1  through 50 3. the list ['a', 'bb', 'ccc'] create a new list that ends 26 letters of z 

l1 = []
l2 = []
l3 = []

for i in range(51):
    l1.append(i)

for i in range(51):
    l2.append(i**i)
    
for i in range(27):
    l3.append(chr(i+96)*i)

print(f"The list of numbers from 0 - 50 is: {l1}")
print(f"The square list of numbers from 0 - 50 is: {l2}")
print(f"The list of a-bb-ccc... {l3}")