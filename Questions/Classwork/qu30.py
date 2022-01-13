#WAP tht creates a dict of radius of circle and its circumference 
d = {}
while True:
    r = float(input("Enter the radius of circle: "))
    if r not in d: 
        key = r
        c = 2 * 3.14 * r
        d[key] = c
    print(d)
    print()