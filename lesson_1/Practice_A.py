#תרגיל 1.

print('"Net4U,  is the best place\n      ...in the world"\n\n\n')

#תרגיל 2.

import datetime

print(datetime.datetime.now())

#תרגיל 3.

f_name = input("\n\nEnter your first name: ")
l_name = input("Enter your last name: ")
f_name2 = ' '.join(f_name[::-1])
print(f_name2)
l_name2 = ' '.join(l_name[::-1])
print(l_name2)

#תרגיל 4.

file = input("\n\nEnter filename: ")
f_extns = file.split(".")
print(f_extns)
print("The extesion of the file is : " + repr(f_extns[-1]))


#תרגיל 5.

n= int(input("\n\ninsert an integer : "))
n1 = int( "%s" % n)
n2 = int("%s%s" % (n, n))
n3 = int("%s%s%s" % (n, n, n))
print(n1 + n2 + n3)

#תרגיל 6.

given_num = int(input("Enter a number : "))
if given_num%2 == 0:
    print("I AM EVEN")
elif given_num % 2 == 1:
    print("I AM ODD")

#תרגיל 7
print("Input your height: ")
h_fit = int(input("Feet : "))
h_inch = int(input("Inches: "))
h_inch += h_fit*12
h_cm = round(h_inch*2.54, 1)

print("your height in centimeter : %d cm." %h_cm)

#תרגיל 8

n = 20
d = {"x": 200}
l = [1,3,5]
print(type(n)())
print(type(d)())
print(type(l)())

#תרגיל 9

My_dict = {0:10, 1:20}
My_dict.update({2:30})
print(My_dict)

#תרגיל 10


from collections import defaultdict, Counter
str1 = 'Net4U'
my_dict1 = {}
for letter in str1[0],str1[1],str1[3],str1[4]:
    my_dict1[letter] = my_dict1.get(letter, 1)
    for letter in str1[2]:
        my_dict1[letter] = my_dict1.get(letter, 2)
print(my_dict1)