#for loops

#for i in range(1,11,2):
#    print(i)

#list_eran = ["banaba", "apple", "mango"]
#for x in list_eran:
#   print((x))

#list_eran2 = ["ball", "pen", "pencil"]
#for x in range(len(list_eran2)):
#    print(list_eran2[x])

from time import sleep

print("Now we will get all the details about your class:\n----------------------------------------------------\n")
for i in range(4):
    NAME=input("Enter a name:")
    AGE= int(input("Enter age:"))
    PHONE=input("Enter a phone:")
    print("Printing student number " + str(i+1)  + " Details... \n")
    sleep(3)
    print("Full name: " + NAME + "\nAge: " + str(AGE) + "\nPhone: " + PHONE + "\n---------------------------\n")



