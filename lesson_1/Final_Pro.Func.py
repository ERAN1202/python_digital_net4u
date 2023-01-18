'''create a menu:
a. IP system?
b. DNS system?

a
====
   1. search for IP address from a list
   2. add IP address to a list
   3. delete IP address to a list
   4. print all the IPs to the screen

b
===
    1. serach for URL from a dictionary
    2. add URL + IP address to a dictionary
    3. delete URL from a dictionary
    4.update the IP address of specific URL
    5. print all the URL:IP to the screen'''


from time import sleep



def menu():
    while(True):
        choice_1=input("Menu:\n------------\na. IPSystem\nb. DNS System\n")
        if (choice_1 == "a"):
            choice_2 = input("Menu IP System:\n-----------\n1.search IP\n2.add IP\n3.delete IP\n4.Print all IP ")
            if choice_2 == "1":
                search_ip()
            elif choice_2 == "2":
                add_ip()
            elif choice_2 == "3":
                delete_ip()
            elif choice_2 == "4":
                print_IPs()

        elif (choice_1 == "b"):
            choice_3 = input("Menu DNS system:\n--------------\n1.search URL\n2.add IP+URL to dict.\n3.delete URL from dict.\n4.update IP address spec. URL\n5.print all the URL:IP to the screen")
            if choice_3 == "1":
                search_URL()
            elif choice_3 == "2":
                add_ip_URL()
            elif choice_3 == "3":
                delete_URL()
            elif choice_3 == "4":
                update_IPs()
            elif choice_3 == "5":
                print_URL()


        else:
            print("Enter a/b only")
            continue
        exit=input("Do you wnat to exit? yes/no")
        if (exit == "yes"):
            print("ByeBye")
            break

def search_ip():
    print("1")

def add_ip():
    ip_added = input("IP add is : ")
    print(str(ip_added))
    filename = "C:/Users/eranb/Desktop/IP.txt"
    file = open(filename, "a")
    file.write(ip_added)
    file.close()
    file = open(filename, "r")
    file.read()
    file.close()



def delete_ip():
    print("3")

def print_IPs():
    print("4")

def search_URL():
    print("1")

def add_ip_URL():
    print("2")

def delete_URL():
    print("3")
def update_IPs():
    print("4")

def print_URL():
    print("5")

menu()



