#WAP tht has a nested tupple toppers details edit and reprint the details
t = (("arnav", "BE", 92.02), ("chaitanya", "BCA", 99.0), ("Dhruvika", "BTech", 97))
nt = ()
for i in t: 
    print(i)
print()
c = input("Do u want to change anything? (Y/y): ")
print()
if c == 'y' or c == 'Y':
    n = input("Enter the present name: ")
    ni = input("Enter the correct name: ")
    nc = input("Enter the correct course: ")
    na = input("Enter the correct marks: ")
    i = 0
    while i < len(t):
        if t[i][0] == n:
            nt += (ni, nc, na)
        else: 
            nt+t[i]
        i+=1
for i in nt:
    print(i, end=" ")
