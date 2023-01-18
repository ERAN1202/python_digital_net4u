#my_list = []
#filename = "C:/Users/eranb/Desktop/eran.txt" # # במשתנה אני שם את נתיב הקובץ
#file = open(filename, "r")#   אני מגדיר משתנה כדי שיהיה שמור לי בזכרון ואוכל לעבוד עליו, במשתנה אני מבקש לפתוח את הקובץ + איזו הרשאה
#for line in file:#קריאת שורות שורות בקובץ
#    print (line)
#    my_list.append(line)
#file.close()
#print(my_list)

filename = "C:/Users/eranb/Desktop/eran.txt" # # במשתנה אני שם את נתיב הקובץ
file = open(filename, "r")#   אני מגדיר משתנה כדי שיהיה שמור לי בזכרון ואוכל לעבוד עליו, במשתנה אני מבקש לפתוח את הקובץ + איזו הרשאה
new_list=[]
new_list =file.read().splitlines()
print(type(new_list))
print(new_list)
file.close()

for i in new_list:
    print(i)

filename = "C:/Users/eranb/Desktop/eran.txt"
file = open(filename, "r")
print(file.read(3))
file.close()

#יצירת קובץ באמצעות "x"

#filename = "C:/Users/eranb/Desktop/eran_2.txt"
#file = open("C:/Users/eranb/Desktop/eran_2.txt", "x")
#file.close()

#קריאה לשורה ספציפית מתוך קובץ
filename = "C:/Users/eranb/Desktop/eran_2.txt"
file = open(filename, "r")
print((file.readlines()))
file.close()