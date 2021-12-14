#Write a program to accept comma separated words and store and print unique words in a sorted order (alphabetically)

s = input("Enter words seperated by comma: ")
l1 = list(s.split(","))
print(sorted(l1))