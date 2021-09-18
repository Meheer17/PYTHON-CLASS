#WAP to identify and calculate roots of a quadratic equation

a = int(input("enter the a val: "))
b = int(input("enter the b val: "))
c = int(input("enter the c val: "))
D = (b*b)-(4*a*c)
d=2*a

print("\n")
if D>0:
  print("REAL ROOTS")
  root1 =(-b+d**0.5)/d
  root2 =(-b-d**0.5)/d
  print("\n")
  print("Root1= ",root1 ,"\n" ,"Root2= ",root2)

elif D ==0:
  print("EQUAL ROOTS")
  root=-b/d
  print("\n")
  print("Root1 and Root2= ",root)

else :
  print("No Roots")