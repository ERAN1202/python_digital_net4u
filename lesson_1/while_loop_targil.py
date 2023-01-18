'''num=int(input("enter a number: "))
while(num!=7):
    print(num*100)
    num = int(input("enter a number: "))

counter=10

while counter>0:
    print(counter*100)
    print("eran bar haim")
    counter -= counter

while(True):
    name=input("enter a name: ")
    if name == "Eran":
        print("hello Eran")
        break
    elif name == "Ben":
        print("Hello Ben")
        continue
    else:
        print("where is Eran?")

    number=int(input("Enter a number: "))
    print(number*100)

print("Bye Bye ....")
'''
while(True):
    CHOICE = input("Menu:\n1.insert number and ** it by 3\n2.insert 4 IPs to a list and print it\n3.insert 4 entries to DNS_Dictionary and print it\n4.check if a string is polindrom\n")
    if (CHOICE == "1"):
        print("The new number is: " + str((int(input("enter a number: ")))**3))
    elif (CHOICE == "2"):
        ip_list = []
        ip_list.append(input("Enter new IP: "))
        ip_list.append(input("Enter new IP: "))
        ip_list.append(input("Enter new IP: "))
        ip_list.append(input("Enter new IP: "))
        print("The new list: \n" + str(ip_list))
    elif (CHOICE == "3"):
        dns_dict  = {}
        dns_dict.update({input("Enter URL: ") : input("Enter an IP.ADD: ")})
        dns_dict.update({input("Enter URL: "): input("Enter an IP.ADD: ")})
        dns_dict.update({input("Enter URL: "): input("Enter an IP.ADD: ")})
        dns_dict.update({input("Enter URL: "): input("Enter an IP.ADD: ")})
        print("\nThe new dns_dict:\n---------\n" + str(dns_dict))
    elif (CHOICE == "4"):
        word = input("Enter a word: ")
        if word == word[::-1]:
            print("This is a polindrom")
        else:
            print("This isnt polindrom")
    else:
        print("enter 1-4 only!")

    exit = input("Do you want to exit? y/n : ")
    if (exit == "y" or exit == "yes"):
        break
    else:
        print("Welcome back")