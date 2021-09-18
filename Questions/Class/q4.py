#4. Write a program to calculate salary of an employee given his basic pay (to be entered by the user), HRA-10 percent of basic 
basic=float(input("Enter the basic pay of an employee: "))
TA = basic*5/100
HRA = basic*10/100
salary = basic+HRA+TA
print("Employee Details:")
print("Basic Pay=", basic, "\tHRA=", HRA, "\tTA=", TA, "\nTotal Salary of the employee=", salary)