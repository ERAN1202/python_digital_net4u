from random import  randint

def calculating(a,b):
    c=int(input("Enter a number: "))
    sum = a*b*c
    print("The sum is : " + str(sum))

def dogs_age(a):
    print("Real dog age is: " +str(a*7))



def menu():
    choice=input("Menu: \n1.printing 1-100\n2.random 2 cubes")
    if (choice == "1"):
        for i in range(1,101):
            print(i)
    elif (choice == "2"):
        print("Cube 1: " + str(randint(1, 6)))
        print("Cube 1: " + str(randint(1, 6)))

menu()




