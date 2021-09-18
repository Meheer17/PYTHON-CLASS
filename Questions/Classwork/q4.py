#WAP a program to input if its a leap year or not.

num = int(input("Enter the year: "))

if (num % 4) == 0 and (num % 100) !=0 or (num % 400) == 0:
  print("THAT IS A LEAP YEAR")
else:
  print("THAT IS NOT A LEAP YEAR")  