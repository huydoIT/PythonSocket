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

accA = 1500
accB = 300
accC = 750
accD = 2500
with conn:
    try:
        # in ra thông địa chỉ của client
        print('Connected by', addr)
        while True:
            msg = ""
            # Đọc nội dung client gửi đến
            data = conn.recv(1024)
            cmd = data.decode()
            if data.decode() == 'END':  # nếu không còn data thì dừng đọc
                print("Client disconnected!\n")
                break
            elif cmd[0] == 'W' and cmd[1] == 'A':
                accA += int(cmd[2:])
                conn.sendall('Transaction completed!'.encode())
            elif data.decode() == 'RA':
                conn.sendall(str(accA).encode())
            elif data.decode() == 'RB':
                conn.sendall(str(accB).encode())
            elif data.decode() == 'RC':
                conn.sendall(str(accC).encode())
            elif data.decode() == 'RD':
                conn.sendall(str(accD).encode())
            else:
                conn.sendall('Account do not exist!\n'.encode())
            # In ra Nội dung
            print('Client: ', data.decode())

    finally:
        s.close()  # đóng socket
