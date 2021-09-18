#WAP to enter any number and check it is armstrong or not

a = input("Enter a value: ")
l = len(a)
b = int(a)
c=b
d=0
i=1
while i<=l:
        digit=b%10
        d+=digit**l
        b=b//10
        i+=1
print(f"Evaluated val: {d}")   
if c==d:
        print("The entred no. is an armstrong number.")
else: 
        print("The entred no. is not a armstrong number.")