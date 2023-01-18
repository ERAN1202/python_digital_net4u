print("עכשיו נחשב את התקציב :\n\nמחירים:\n----------\nעגבניה = 3 ש"ח\nמלפפון = 2 ש"ח\nקולה = 5 ש"ח\ncעוף = 20 nis\n")
tomatos = int(input("how many tomatos?"))
cucumbers = int(input("how many cucumbers?"))
cola = int(input("how mach cola?"))
chickens = int(input("how many chicken?"))

print("\nsummery of your order:\n---------\ntomatos: "  + str(tomatos) + "\ncucumbers: " + str(cucumbers) + "\ncola: " + str(cola) + "\nchickens: " + str(chickens))
sum1 = tomatos*3
sum2 = cucumbers*2
sum3 = cola*5
sum4 = chickens*20

summery = sum1 + sum2 + sum3 + sum4
print("\nyour total payment : " + str(summery))

print("\nplus tax : " + str(summery*1.17))


