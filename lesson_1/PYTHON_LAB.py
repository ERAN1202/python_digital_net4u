
def marketing_budget():
    print("ADVERTISING CAMPAIGN -" + "\n======================")
    FB_cost = (int(input("Facebook campaign budget per day in ILS=  " )))
    print(str(FB_cost) + "ILS")
    long_fbcamp = int(input("How many days you want FACEBOOK campaign will run? "))
    print(str(long_fbcamp) + " days")
    INST_cost = int(input("Instagram campaign budget per day in ILS = "))
    long_inscamp = int(input("How long you want INSTAGRASM campaign will run ? "))
    Total_Budget = int(input("Enter your total budget: "))

    sum_camp = ((FB_cost*long_fbcamp) + (INST_cost*long_inscamp))
    print("The total cost of the campaign is : " + str(sum_camp) + "ILS" + "\nPLUS TAX: " + str(sum_camp*1.17))


    if (sum_camp) > (Total_Budget):
        print("Add a : " + str(sum_camp - Total_Budget) + "ILS to your budget\n\n\n")
    else:
        print("succesfull\n\n\n")


marketing_budget()

from time import sleep
from random import randint

def lottery_game():
    guess_no = [2,5,6,11,12,31]
    print( " YOUR GUESSING NUMBERS IS :" + str(guess_no))
    game_cost = int(input("LOTTERY GAMES ROW COST IN ILS:"))
    lottery_budget = int(input("HOW MUCH MONEY DO YOU HAVE ? "))
    num_of_rows = lottery_budget//game_cost
    sleep (2)
    print("YOU HAVE : " + str(num_of_rows) + " ROWS TO PLAY")
    sleep (2)
    price = 0

    for i in range(num_of_rows):
        print("GAME NUMBER: " + str(i+1) + "\n-------------\n")
        sleep (2)
        win_num = sorted([randint(1, 37) for x in range(6)])
        print("THE WINNING NUMBERS ARE : " + str(win_num))
        check_num = 0
        for i in win_num:
            if i in guess_no:
                check_num += 1
        if check_num == 6:
            price = price + 1
            print("YOU WON " + str(price) + "M ILS")
        elif check_num == 5:
            price = price + 5000
            print("YOU WON " + str(price) + " ILS")
        elif check_num == 4:
            price = price + 100
            print("YOU WON " + str(price) + " ILS")
        elif check_num == 3:
            price = price + 10
            print("YOU WON " + str(price) +  "ILS")
        else:
            print("NEXT TIME")

    print("calculating your price...")
    sleep(3)
    print("your price : " + str(price) + "ILS")



lottery_game()


