def add(x, y):
    return x+y
'''
כתיבת הפונקציה לעיל בתוך פונק' למדא
'''

print((lambda x, y: x + y) (2, 5))

import functools

shopping_list = [ 100, 220, 300, 350,35]
print(functools.reduce(lambda x, y: x + y, shopping_list))
'''במקום פןנקצ add נכתוב אותה בצורת למדא'''

my_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(list(filter(lambda x: x % 2 == 0, my_list)))

'''כאן ניתן לתת כארגומנט את הפונק' למדא לתוך הפונק'filter
'''

list_of_tuples = [(2, 3), (1, 4), (3,5), (4,2)]
print(sorted(list_of_tuples, key=lambda x: x[1]))




'שימוש בלמדא-הכדרה שלה בתור איבר בתוך מבנה נתונים'
cal_square_list = [lambda x: x**2, lambda x: x**3, lambda  x: x**4]
for func in cal_square_list:
    print(func(3))

a = lambda x: 1
print(a(4))
print(a("s"))
print(a(2))
print(type(a(3)))

b = lambda x: x
print(b(1))
print(b(3))

import functools
def function(num, item):
    return num + 1
password = input("Enter Your password (integers only): ")
lst = list(map(int, password))
magic = functools.reduce(function, lst)
result = (lambda x: x % 4 == 0)(magic)
if result:
    print("Correct password!")
else:
    print("Wrong password.")