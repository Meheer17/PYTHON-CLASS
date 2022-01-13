#WAP to create 2 dict. one stores conversion values from meters to centimeter and the other stores values from centimeter to meters

ctm = {}
mtc = {}
while True:
    print("\n1. Centimeter to Meter \n2. Meter to Centimeter \n3. Display the Dict \n4. Quit \n")
    c = int(input("Enter your choice: "))

    if c == 1:
        val = float(input("Enter the value: "))
        t = val/100
        ctm[val] = t

    elif c == 2: 
        val = float(input("Enter the value: "))
        t = val * 100
        mtc[val] = t

    elif c == 3:
        print(ctm)
        print(mtc)

    elif c == 4:
        break
 
    else:
        print("invalid choice..")