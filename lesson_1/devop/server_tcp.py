import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("The server is up and running")

(client_socket, client_address) = server_socket.accept()
print("Client connected")

while True:
    data = client_socket.recv(1024).decode()
    print("Client send:" + data)
    if data == "Quit":
        print("closing client socket now...")
        client_socket.send("Bye".encode())
        break
    client_socket.send(data.encode())

client_socket.close()
server_socket.close()