'''menu
1.dogs details
2.friends list
3.Atzeret
'''
from random import randint
from  time import sleep
def menu():
    while(True):
        choice=input("Menu:\n-------\n1.Dogs details\n2.Friends list\n3.Atzeret\n")
        if choice == "1":
            Dogs()
        elif choice == "2":
            friends()
        elif choice == "3":
            Atzeret()
        else:
            print("Enter 1-3 only!")
            continue
        exit=input("Do you want to exit? yes/no\n ")
        if exit == "yes":
            break
        else:
            print("Enter your choice again")
    print("Bye Bye")

def Dogs():
    name=input("Enter a dog's name: ")
    age=int(input("Enter a dog's age:"))
    print("Dog name is = " + name + "\nDog age is = " + str(age*7))

def friends():
    friends_list = []
    for i in range (3):
        friends_list.append(input("Enter a name: "))
        name=input("Enter a new name: ")
    if name in friends_list:
        print( name + " It's already in")
    else:
        print( name + " It's a new name")

def Atzeret():
    num=int(input("Enter a number: "))
    sum=1
    for i in range(1, num + 1):
        sum=sum*i
    print(str(num) + " Atzeret is: " + str(sum) + "\n" )


menu()



