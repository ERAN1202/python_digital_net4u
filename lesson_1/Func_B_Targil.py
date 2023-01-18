# פונצקיות שלא מקבלות ערך אבל כן מחזירות ערך

'''def calculating():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    sum=num1*num2
    print("Your number is: " + str(sum))
    return sum

a=calculating() + 29
print("WOW:" + str(a))
'''
# פונקציה שמקבלת ערכים ומחזירה ערכים

def calculate2(x,y):
    print("Your first number: " + str(x) + "\nYour second number: " + str(y))
    print("\nYour new number is: " + str(x**y))
    sum=x**y
    print("Your number is: " + str(sum))
    return sum

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
eran=calculate2(a, b) + 29
print("Wow:" + str(eran))

'''

def add_ip(list, ip1, ip2, ip3):
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list

ip_list=[]
ip_n1=input("Enter 1st IP: ")
ip_n2=input("Enter 2nd IP: ")
ip_n3=input("Enter 3rd IP: ")
ip_list=add_ip(ip_list, ip_n1, ip_n2, ip_n3)
print(ip_list)

'''