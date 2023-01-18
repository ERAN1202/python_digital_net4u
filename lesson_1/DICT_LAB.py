'''create a dictionary with 5 namse & money
then sum the money of the first & last names and print it to the screen
after, add a new name with the sum of the money you calculated before
in the end, print the number of entries and check if "eran" is inside
'''
my_shop_list = {"tomato":5,"potato":3,"lemon":6,"melon":7,"orange":10}
print(my_shop_list)
summery = my_shop_list["tomato"] + my_shop_list["orange"]
print("The summery is : " + str(my_shop_list["tomato"] + my_shop_list["orange"]))
my_shop_list.update({"chicken": 12, "beaf": 25})
print(my_shop_list)
print("Number of entries: " + str(len(my_shop_list)))
print( "tomato" in my_shop_list)