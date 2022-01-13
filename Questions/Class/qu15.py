#WAP to take a list and then do these following stuff... 1. update val 2.insert val 3. delete  4 exit 

def update(list):
    print(l)
    val = int(input("Element to be updated: "))
    uval = int(input("To val: "))
    for i in range(len(l)):
        if l[i]==val:
            l[i]=uval
    print(l)
    print()

def insert(list):
    ins = int(input("Enter the val to insert: "))
    l.append(ins)
    print(c)
    print()

def delw(list):
    print(l)
    hunt = int(input("Enter the val to delete: "))
    for i in l:
        if i == hunt: 
            l.remove(i)
    print(l)
    print()

l = eval(input("Enter the number list: "))
print()
print(f"The list is {l}")
print()

while True:
    print(" 1. Update val in the list \n 2. Insert element to list \n 3. Delete an element \n 4. Exit \n")
    c = int(input("Enter your choice: "))
    print()
    if c == 1:
        update(l)
    elif c == 2:
        insert(l)
    elif c == 3:
        delw(l)
    else: 
        break