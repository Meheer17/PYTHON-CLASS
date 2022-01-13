#WAP tht has a dict of states and their codes. Add another state in pre-defined dict, print all the items in the dict and try to print codes for a state that does not exist. set a default value prior to print

os = {"Karnataka":"KA", "Delhi":"DL", "Maharastra":"MH"}
os["Tamil Nadu"] = "TN"
print(f"The states persent in the list: {os}\n")
os.setdefault("Rajasthan", "Sorry no idea...")
print(f"Code for Karnataka is: ", os["Karnataka"])
print()
for i in os.items():
    print(i ,end="\n")
print()
card = int(input("Enter 1 if u want to update, Enter 2 if u want to exit: "))
print()
while card == 1:
    s = input("Enter the state name: ")
    s = s.capitalize()
    if s not in os:
        c = input("Enter the state code: ")
        c = c.upper()
        os[s]=c
        print(os)
        print()
        card = int(input("Enter 1 if u want to update, Enter 2 if u want to exit: "))
        print()
    else:
        print()
        print(s,os[s])
        print()