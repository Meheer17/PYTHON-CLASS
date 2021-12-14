# find the largest word from input
def biggo(a):
    big = 0
    for i in words: 
        l = len(i)
        if big < l:
            big = l
            bw = i
    print(f"Largest Word is {bw}")

a = input("Enter your string: ")
words = a.split()
biggo(a)