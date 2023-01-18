def combine_coins(coin, numbers):
    output = ''
    for num in numbers:
        output += coin + str(num) + ', '
    return output[:-2]

print(combine_coins("$",[0,1,2,3,4]))

def combine_coins(coin, numbers):
    return str(coin) + str(numbers)

l1 = ['$' ,'$', '$', '$','$']
l2 = [0, 1, 2, 3, 4]
print(list(map(combine_coins,l1,l2)))



def square(num):
    return num **2

list_of_numbers = [2,3,4,5,6]
new_list = []
for number in list_of_numbers:
    new_list.append(square(number))

print(new_list)

def square(num):
    return num **2
list_of_numbers = [2,3,4,5,6]
result = map(square,list_of_numbers)
print(list(result))

def double(char):
    return char*2

def double_letter(my_str):
    result1 = map(double, my_str)
    return ''.join(result1)


print(double_letter("python"))
print(double_letter("we are the champions!"))


def number_1(num):
    if num % 4 == 0:
       return num

def four_dividers(number):
           return list(filter(number_1,(range(1,number))))

print(four_dividers(9))
print(four_dividers(3))


def sum_of_digits(num):
    return sum(map(int, str(num)))

print(sum_of_digits(104))