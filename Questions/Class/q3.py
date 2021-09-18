#3. Write a program to read two floating point numbers. Add these numbers and assign the result to an integer. 2 Finally display the value of all the three variables....

num1 =float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))
sum1=int(num1+num2)
print("The sum of {} and {} is {}".format(num1, num2, sum1))