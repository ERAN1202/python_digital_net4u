print(chr(95))
print(ord("a"))
print(ord("a") + 2)
print(chr(ord("a") - 2))


new_password = []
password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
for i in password:
    new_password.append(chr(ord(i) + 2))

print(''.join(new_password))

new_password = []
password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
decode_pass = [new_password.append(chr(ord(i) + 2)) for i in password]
print(''.join(new_password))


def intersection(list_1, list_2):
    return set([i for i in list_1 if i in [j for j in list_2]])




def split_data(msg, expected_fields):
    """
    Helper method. gets a string and number of expected fields in it. Splits the string
    using protocol's data field delimiter (|#) and validates that there are correct number of fields.
    Returns: list of fields if all ok. If some error occured, returns None
    """
    j = 0
    data_list =list(msg)
    for char in data_list:
        if char == "#":
            j += 1
        if j == expected_fields:
           print(msg.split("#"))
        else:
            return None

print(split_data("username#password" , 1))
split_data("user#name#pass#word" , 2)
split_data("username" , 2)


import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 8820))

data = ""
while data != "Bye":
    msg = input("please enter your message\n")
    my_socket.send(msg.encode())
    data = my_socket.recv(1024).decode()
    print("The server sent" + data)

my_socket.close()


