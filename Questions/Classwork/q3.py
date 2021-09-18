#WAP to enter monthly sale of a Salesman and give him commision that is if the monthly sale is more tha 5L then commison will be 10% of monthly sale other wise 5%.

sale = float(input("Enter the total sales: "))

if sale > 500000:
  print("Bonus: ", sale * (10/100))
else:
  print("Bonus: ", sale *(5/100))  