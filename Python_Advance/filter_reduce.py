#list of file name

my_files=["eran.mp3", "yuval.txt" ,"avigal.txt" ,"ilanit.mp3"]

def is_mp3_file(filename):
    return filename.endswith(".mp3")

print(list(filter(is_mp3_file, my_files)))


import functools

def add(x,y):
    return x + y
shopping_list = [ 100, 220, 300, 350,35]
print(functools.reduce(add, shopping_list))

def func(x):
    return x % 2 != 0
print(list(filter(func, range(10))))

def func(value):
    x = 0
    try:
        x = 1
        print("m"+ value)
        x = 2
        print(x)
    except:
        print(x)
func(3)


gen = (i / 2 for i in [0, 9, 21, 32])
print(next(gen))
print(next(gen))
print(next(gen))
