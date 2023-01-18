filename = "C:/Users/eranb/Desktop/eran_1.txt"
with open(filename, "w") as filename:
    i = 0
    while (i <= 5):
        i = i+1
        filename.write("data inside file\n")
        break


