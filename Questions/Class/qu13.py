#WAP takes a word sep by comma and prints unique words in sorted order 

def sep(words):
    for i in words:
        if i not in w:
            w.append(i)
        else: 
            continue

words = eval(input("Enter words with comma: "))
w = []
sep(words)
print(w)
w.sort()
print(f'Sorted order of the sentence is {w}') 