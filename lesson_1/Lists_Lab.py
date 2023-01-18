'''
create a list with 4 details about you: name,age,mail,phone and print it to the screen
then create another list with 2 IPs the add 3 more IPs, pop the 3rd IP and print how many
IPs do we have and print them
'''
my_detail = ["eran", 43, "eranbarhaim@yahoo.com", "0524660200"]
print(my_detail)
print("my name: " + my_detail[0] + "\nage : " + str(my_detail[1]) + "\nmail: " + my_detail[2] + "\nphone no:" + my_detail[3])

ip_list = ["192.168.1.1" , "10.10.10.1"]
print(ip_list)
ip_list.append("192.168.1.2")
ip_list.append("192.168.1.3")
ip_list.append("10.10.10.2")
print(ip_list)
ip_list.pop(2)
print("Ip list lengtgh is: " + str(len(ip_list)) + "\nThe IP list : " + str(ip_list))