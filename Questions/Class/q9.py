# To read the number untill -1 is emcountred. Also the "-ve", "+ve", and zeros entered

neg_count = pos_count = zero_count = 0

while(True):
    num = int(input("Enter the number: "))
    if(num == -1):
        neg_count += 1
        break
    elif(num == 0):
        zero_count += 1
    elif(num > 0):
        pos_count += 1
    else:
            neg_count+=1

print()
print(f"Number of positive numbers: " ,pos_count)
print(f"Number of negative numbers: ",neg_count)
print(f"Number of zeros: ",zero_count)