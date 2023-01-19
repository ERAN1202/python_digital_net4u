'''a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
x = (-b+(b**2-4*a*c)**1/2)/(2*a)
print(x)
'''


num_of_word = 1
while True:
    num_of_word += 1
    word = input("הקלידי מילה/משפט: ")
    word_2 = word[::-1]
    if word == word_2:
        print("זהו פולינדרום")
    else:
        print("זו מילה רגילה")

    exit = input("אביגולש,תרצי לצאת?כן/לא ")
    if (exit == "כן"):
        print("נתראה בפעם הבאה")
        break
    else:
        print("החלי סבב נוסף")

print("goodbye")

