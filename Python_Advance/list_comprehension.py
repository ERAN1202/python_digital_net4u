'''יצירת רשימה של הרווחים הצפויים לי בהעלאה בריבוע
נשתמש בלולאה כשההנחה היא כ האפשרות לפתירת תרגילים היא עד 100'''
import functools
my_money_list =[]
for i in range(100):
    my_money_list.append(i**2)
print(my_money_list)

'''איך נכתוב את הקוד לעיל בשורה אחת, יש מה שנקרא "הרכבת רשימה(list comprehesion)'''

my_money_list = [x**2 for x in range(100)]
print(my_money_list)

sentence = "אביגל בר חיים המהממת"
words = sentence.split()
secret = [word[0] for word in words if word != "חיים"]
print(secret)

class Question:

    def __init__(self):
        self.a = 0

    def func(self):
        print(self)

def main():
    A = Question()
    A.func()

main()

import functools

def intersections(list_1, list_2):
    return list(set(list_1).intersection(list_2))
    #return set([x.intersection(y)  for x in list_1 for y in list_2])

def intersection_1(list_1, list_2):
    return set([i for i in list_1 if i in [j for j in list_2]])

print(intersections([1, 2, 3, 4], [8, 3, 9]))
print(intersections([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))

print(intersection_1([1, 2, 3, 4], [8, 3, 9]))
print(intersection_1([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))

def is_prime(number):
    return set([True if number%i == 0 else False for i in range(2, number)])=={False}

print(is_prime(42))
print(is_prime(43))

def is_funny(string):
    for char in string:
        if char != 'h' and char != 'a':
            return False
    return True

def is_funny_2(string_1):
    return set([False if char_1 != 'h' and char_1 != 'a' else True for char_1 in string_1])=={True}

print(is_funny("hahahahahah"))

print(is_funny_2('hahahah'))