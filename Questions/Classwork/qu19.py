#WAP to find the sum of numbers 
max = int(input("Enter the max number: "))
tot = 0
for i in range(1, max+1, 2):
    tot += i
print(f"Sum of numbers from 1 to {max} = {tot}")