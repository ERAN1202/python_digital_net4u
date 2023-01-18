'''נקבל כקלט כמה כסף יש לנו לשחק
עלות משחק 3 שח
אם יש עודף נחזיר ללקוח
בכל תור נגריל 2 קוביות אם הן זהות זכינו ב 100 שחתאם הן זהות וגם שוות ל6 זכינו ב 1000 שח
אם הן לא זהותתאבל קוביה2 שווה ל- 2 זכינו ב 40 שח
אם הן לא זהות אבל קוביה 1 שווה ל- 1 זכינו ב 20 שח
לבסוף נדפיס למסך בכמה זכינו
'''
from random import randint
from time import sleep

print("wlecome to cube game\nEach game cost 3 ILS\n")
money= int(input("how much money do you have?"))
turns= (money//3)
print("you have " + str(turns) + " games to play\nyour change is: "+ str(money%3) + " ILS\n")
price = 0


for i in range(turns):
    print("Round number: " + str(i+1) + " :\n--------------\n")
    sleep(3)
    cube1=randint(1,6)
    cube2=randint(1,6)
    print("Cube 1 : " + str(cube1) + "\nCube 2 : " + str(cube2) + "\n")
    if (cube1 == cube2 and cube1 == 6):
        price = price + 1000
    elif cube1 == cube2:
        price = price + 100
    elif (cube1 != cube2 and cube2 == 2):
        price = price + 40
    elif(cube1 != cube2 and cube1 == 1):
        price = price + 20
    elif (cube1 == 1 and cube2 == 2):
        price = price + 60

print("calculating your price...")
sleep(3)
print("your price : " + str(price))
