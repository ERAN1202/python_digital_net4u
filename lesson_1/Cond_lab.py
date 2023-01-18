from time import sleep

'''name = input("enter your name:  \n")
if name == "eran":
    print("hello eran\n")
elif name == "avigal":
    print("hello big daughter\n")
elif name == "ilanit":
    print("hello my wife\n")
elif name == "yuval":
    print("hello young daughter\n")
else:
    print("where is my family?")

print("love you family")
'''
''' write a code that will show the menu:
    menu:
    1.insert number and ** it by 3
    2.insert 4 IPs to a list and print it
    3.insert 4 entries to DNS_Dictionary and print it
    4.check if a string is polindrom
    
    if the user wont choose 1-4 ypu will tel him to insert 1-4 only!
    '''

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
    print("2")
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