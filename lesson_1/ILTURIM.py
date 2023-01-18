file_path = "C:/Users/eranb/Desktop/eran_1.txt"
with open(file_path,"r") as file_path:
    data=file_path.read()
    print("the file contain: " + data)

fruit = "apples"
drink = "wine"
print("the basket contains %s and %s." %(fruit, drink))
print("the basket contains: " + fruit + " and " + drink + ". ")
bottle_num, drink = 3 , "wines"
print("the basket contains: %s bottles of %s." %(bottle_num, drink))

