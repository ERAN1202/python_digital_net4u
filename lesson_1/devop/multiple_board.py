from random import randint
from time import sleep

def mult():

    while(True):
        choice = input("1.תרגילים עבור אביגל""\n2.תרגילים עבור יובל\n\nהקלידי את בחירתך:\n")
        sleep(0.5)
        if choice == "1":
            num_of_exercise = 1
            grade = []
            while num_of_exercise <= 10:
                num_of_exercise += 1
                num_1 = randint(1,10)
                num_2 = randint(1,10)
                num_3 = num_1*num_2
                print(num_1, "X", num_2, " = ")
                outcome = int(input("התוצאה היא :"))
                if outcome == num_3:
                    sleep(0.5)
                    print("כל הכבוד אביגל")
                    grade.append(10)
                    #print(str(grade) + "נקודות")
                    Sum = sum(grade)
                    print("נקודות", Sum)
                else:
                    sleep(0.5)
                    print("לא נורא מאמי,בפעם הבאה")
                sleep(1)

            exit = input("אביגולש,תרצי לצאת?כן/לא ")
            if (exit == "כן"):
                sleep(1)
                print("כל הכבוד אביגל,נתראה בפעם הבאה")
                break
            else:
                print("המשיכי לתרגיל הבא")

        elif choice == "2":
            num_of_exercise = 1
            grade = []
            while num_of_exercise <= 10:
                num_of_exercise += 1
                num_1 = randint(1, 10)
                num_2 = randint(1, 2)
                num_3 = num_1 * num_2
                print(num_1, "X", num_2, " = ")
                outcome = int(input("התוצאה היא:"))
                if outcome == num_3:
                    sleep(0.5)
                    print("כל הכבוד יובל")
                    grade.append(10)
                    # print(str(grade) + "נקודות")
                    Sum = sum(grade)
                    print("נקודות", Sum)
                else:
                    sleep(0.5)
                    print("לא נורא מאמי,בפעם הבאה")
                sleep(1)

            exit = input("יובלבל,תרצי לצאת?כן/לא ")
            if (exit == "כן"):
                sleep(1)
                print("כל הכבוד יובלבל,נתראה בפעם הבאה")
                break
            else:
                print("המשיכי לתרגיל הבא")


mult()



