#  Write a program that creates a list of 10 random integers. Then create two lists - odd list and even list that has all odd
# and even values in the list respectively.

import random

num_list = [] # eval(input("Enter the numbers: "))
print(num_list)

odd_list = []
even_list = []

count = 0

while(count < 10):
    tmp = random.randint(1, 100)
    if tmp not in num_list:
        num_list.append(tmp)

    elif tmp in num_list:
        tmp = random.randint(1, 100)
        num_list.append(tmp)

    count += 1


print(num_list)

for i in num_list:
    if(i % 2 == 0):
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Odd numbers list: {odd_list}")
print(f"Even numbers list: {even_list}")
