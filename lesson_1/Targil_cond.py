'''NAME = input("Enter a name: ")
if(NAME == "eran"):
    print("hello eran\n")
    AGE = int(input("Enter your age: "))
    if (AGE >= 43):
        print("you so old")
    else:
        print("you young for hitech")
else:
    print("who the fuck are you?\n")
'''

name = input("enter your name: \n")
age = int(input("enter your age: \n"))
if name == "eran" and age >= 18:
    print("you can enter to the club")
else:
    print("you are not allowed")