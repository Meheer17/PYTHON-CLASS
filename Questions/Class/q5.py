#Write a program to prepare a grocery bill. for that enter the name of the items purchased,quantity in which it is purchased, and its price per unit. then display the bill in the following format.

print("***ITEMS LIST***")
item_name1 = input("Enter the item name1: ")
quantity1 = int(input("Enter the quantity: "))
item_price1 = float(input("Enter the price: "))
print("\n")
item_name2 = input("Enter the item name2: ")
quantity2 = int(input("Enter the quantity: "))
item_price2 = float(input("Enter the price: "))

total = quantity1 * item_price1 + quantity2 * item_price2 
print("\n")
print("\n")

print("***BILL***")
print("Item Name \t\t Item Quantity \t\t Item Price")
print("\n")
print(item_name1, "\t\t",quantity1, "\t\t", item_price1)
print(item_name2, "\t\t", quantity2, "\t\t", item_price2)
print("\n")
print("\n")
print("***Total Amount***")
print(f"Total amount to be paid: {total}")
