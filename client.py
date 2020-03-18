import socket


HOST = 'localhost'  # Cấu hình address server
PORT = 8000  # Cấu hình Port sử dụng
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cấu hình socket
# ip = input("Input IP address: ")
s.connect((HOST, PORT))  # tiến hành kết nối đến server

while True:
    cmd = input("Client: ")
    mes = str()
    if len(cmd) == 1:
        mes = "R" + cmd
    else:
        if cmd[1] == "O":
            mes = "W" + cmd[0] + str(int(cmd[2:])*(-1))
        elif cmd[1] == "I":
            mes = "W" + cmd[0] + cmd[2:]
        else:
            mes = "Error"
    s.sendall(mes.encode())
    rec = s.recv(1024)
    if not rec:
        print("Done!!\n")
        break
    print("Server: ", rec.decode())
