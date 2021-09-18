#WAP to enter any number and a digit and find out homany times the number is there in the number


a = input("Enter a number: ")
b = input("Enter a digit between 0-9: ")

while (int(b) > 9):
    print ("You have entered an invalid digit.")
    b = input("Enter a digit between 0-9: ")

count = 0

for d in a:
    if d == b:
        count +=1
    else:
        count +=0

print("The number {} in {} comes {} times".format(b,a,count))        