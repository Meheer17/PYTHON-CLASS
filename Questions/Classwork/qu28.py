#wap to count the freqency of a string
a = input("Enter the string :")
b=[]
b=a.split()
c=[b.count(p) for p in b]
print("The frequency of words is ...")
print(dict(zip(b,c)))
