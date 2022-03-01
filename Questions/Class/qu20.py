binary = int(input("Enter the number in binary: "))
decimal, i, n = 0, 0, 0
while(binary != 0):
    dec = binary % 10
    decimal = decimal + dec * pow(2, i)
    binary = binary//10
    i += 1
print(decimal)   

b = 0
m = 1

inp_decimal = int(input("Enter the number in decimal: "))

while inp_decimal >0:
    b = b + ((inp_decimal % 2) * m)
    m = m * 10
    inp_decimal = int(inp_decimal/2)

print(b)
