#WAP to entrer the marks of 4 subs and give out few details
math = float(input("Enter math marks : "))
phy = float(input("Enter phy marks : "))
chem = float(input("Enter chem marks : "))
comp = float(input("Enter comp marks : "))
total = math + phy + chem + comp
agg = (total/4)
print("\n")
print(f'Total = {total} and  Aggregrate Marks {agg}')
print("\n")
if agg>= 75:
  print("Distinction")
elif agg>=60:
  print("First Division")
elif agg >= 50:
  print("Second Division")
elif agg >=40:
  print("Third Division")
else:
  print("Fail")  