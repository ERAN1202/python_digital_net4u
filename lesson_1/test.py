import os
from time import sleep

while (True):
    choice = input("1.create few files in specific folder\n2.run java instalation\n3..insert a resource into resources.txt file\n")
    if choice == "1":
        folder_new = os.getenv('folder')
        os.system('mkdir /home/eran/{} ;ls /home/eran'.format(folder_new))
    elif choice == "2":
        os.system('sudo apt-get install java')
    elif choice == "3":
        os.system('touch resources.txt')
        os.system("free -h | awk 'NR==2 {print $2}' >resources.txt")
        os.system('echo "The storage in the machine is:" ; cat resources.txt')
    else:
        print("Enter 1-3 only")


