# Write a menu-driven program to accept a string from the user to do the following tasks:
#1. Reversing a string
#2. To check whether a given character is present in a string or not
#3. Redisplay the string after removing vowels from it
#4. Count the occurences of a character in a string.

def rev(s):
    r = s[::-1]
    print(f'The rev is {r}')
    print()

def there(s):
    print()
    i = input("Enter the word u want to find: ")
    co = s.split()
    index = 0
    size= len(co)
    while(index < size):
        if co[index] == i:
            print(f"{i} found at {index}")
        else:
            print("Not Found")
            pass
        index += 1
    print()

def vol(s):
    vol = ["a", "e", "i", "o", 'u', "A", 'E', 'I', 'O', 'U']
    index = 0
    h = list(s)
    for i in h: 
        if i in vol: 
            hehe = h.remove(i)
            hehe = "".join(h)
    print(hehe)
    print()

def num(s):
    x = input("Enter the character: ")
    h = list(s)
    val = 0
    for i in h:
        if i == x: 
            val += 1
    print(val)
    print()


s = input("Enter your string: ")
while True:
    print(f" 1. Reversing a string \n 2. To check whether a given character is present in a string or not \n 3. Redisplay the string after removing vowels from it \n 4. Count the occurences of a character in a string. \n 5. to exit \n")

    c = int(input("Enter and of the option btw 1-5: "))

    if c == 1 :
        rev(s)

    elif c == 2 :
        there(s)

    elif c == 3 :
        vol(s)

    elif c == 4:
        num(s)

    else:
        break
