import socket

HOST = 'localhost'  # Cấu hình address server
PORT = 8000  # Cấu hình Port sử dụng
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cấu hình socket
# ip = input("Input IP address: ")
s.connect((HOST, PORT))  # tiến hành kết nối đến server

while True:
    mes = input("Client: ")
    data = mes.encode()
    s.sendall(data)
    rec = s.recv(1024)
    if not rec:
        print("Done!!\n")
        break
    print("Server: ", rec.decode())
