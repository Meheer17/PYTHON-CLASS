#WAP to enter number as long as the user wishes to enter and find the highest and lowest number entred by the user


NumList = []
a = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, a + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
print()
print("The Smallest Element in this List is : ", min(NumList))
print("The Largest Element in this List is : ", max(NumList))
