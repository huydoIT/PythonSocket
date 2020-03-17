import socket
import random
import string


def getSum(a=5, b=4):
    return a + b


def getDev(a, b):
    return a * b


def randStr(num):
    abc = ""
    for i in range(num):
        # upper_alphabet = string.ascii_uppercase
        # random_letter = random.choice(string.ascii_uppercase)
        abc += random.choice(string.ascii_uppercase)
    return abc


HOST = 'localhost'  # Thiết lập địa chỉ address
IP = "127.0.0.1"
PORT = 8000  # Thiết lập post lắng nghe
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cấu hình kết nối
s.bind((IP, PORT))  # lắng nghe
s.listen(3)  # thiết lập tối ta 1 kết nối đồng thời
conn, addr = s.accept()  # chấp nhận kết nối và trả về thông số
with conn:
    try:
        # in ra thông địa chỉ của client
        print('Connected by', addr)
        while True:
            msg = ""
            # Đọc nội dung client gửi đến
            data = conn.recv(1024)
            if 'test' == data.decode():
                msg = data.decode() + "@@@"
                conn.sendall(msg.encode())
                msg = ""
            elif 'AAA' == data.decode():
                msg = data.decode() + "OOO"
                conn.sendall(msg.encode())
                msg = ""
            elif data.decode() == 'END':  # nếu không còn data thì dừng đọc
                print("Client disconnected!\n")
                break
            elif data.decode() == 'hi server':
                while True:
                    mes = input("Server: ")
                    conn.sendall(mes.encode())
                    rec = conn.recv(1024)
                    if rec.decode() == 'OK':
                        break
                    print('Client: ', rec.decode())
            elif 'run' == data.decode():
                for i in range(100):
                    conn.sendall('data sending!!'.encode())
            else:
                # Và gửi nội dung về máy khách
                conn.sendall(randStr(5).encode())
            # In ra Nội dung
            print('Client: ', data.decode())

    finally:
        s.close()  # đóng socket
