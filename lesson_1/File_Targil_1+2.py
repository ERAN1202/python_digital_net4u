'''עבודה עם קבצים'''
'''read  = הרשאה לקרוא מהקובץ
'write = דורס מה שהיה בקובץ/הרשאה שאני יכול לערוך קובץ
append = הוספת נתונים לקובץ
'''

#filename = "C:/Users/eranb/Desktop/eran.txt" # # במשתנה אני שם את נתיב הקובץ
#file = open(filename, "r")#   אני מגדיר משתנה כדי שיהיה שמור לי בזכרון ואוכל לעבוד עליו, במשתנה אני מבקש לפתוח את הקובץ + איזו הרשאה
#print(file.read())
#file.close()# # זה בעצם ישמור לי בקובץ המקורי

#filename = "C:/Users/eranb/Desktop/eran.txt"
#file = open(filename, "w")
#print(file.write("\nilanit bar haim"))
#file.close()

filename = "C:/Users/eranb/Desktop/eran_1.txt" # # במשתנה אני שם את נתיב הקובץ
file = open("C:/Users/eranb/Desktop/eran_1.txt", "r")#  אני מגדיר משתנה כדי שיהיה שמור לי בזכרון ואוכל לעבוד עליו, במשתנה אני מבקש לפתוח את הקובץ + הרשאת קריאה + שינוי בקובץ
#print(file.read())
#file.write("\neran bar haim\nilanit bar haim")
#print(file.read())
#file.close()

#filename = "C:/Users/eranb/Desktop/eran.txt"
#file = open(filename, "a+") # קורא ומוסיף לסוף של הקובץ
#file = open(filename, "a") #   אני מגדיר משתנה כדי שיהיה שמור לי בזכרון ואוכל לעבוד עליו, במשתנה אני מבקש לפתוח את הקובץ + הרשאת הוספה לקובץ
#file.write("\navigal and yuval")
#file.close()

#file = open(filename, "r")#   אני מגדיר משתנה כדי שיהיה שמור לי בזכרון ואוכל לעבוד עליו, במשתנה אני מבקש לפתוח את הקובץ + איזו הרשאה
#print(file.read())
#file.close()# # זה בעצם ישמור לי בקובץ המקורי

#filename = "C:/Users/eranb/Desktop/eran.txt" # # במשתנה אני שם את נתיב הקובץ
#file = open(filename, "r")#   אני מגדיר משתנה כדי שיהיה שמור לי בזכרון ואוכל לעבוד עליו, במשתנה אני מבקש לפתוח את הקובץ + איזו הרשאה
#for line in file:#קריאת שורות שורות בקובץ
#    print (line)
#file.close()

#filename = "C:/Users/eranb/Desktop/eran.txt"
#file = open(filename, "r")
#my_string = file.read()
#file.close()
#print(my_string)
#print(my_string.split(":"))

with open("C:/Users/eranb/Desktop/eran_1.txt", "r+") as file:
    print(file.read())
    file.write("\neran bar haim\nilanit bar haim")
