import socket
import pickle
import connect as cnt


def getAcc(name):
    switcher = {'A': 'accA', 'B': 'accB', 'C': 'accC', 'D': 'accD'}
    return switcher.get(name, "Err")


HOST = 'localhost'  # Thiết lập địa chỉ address
IP = "127.0.0.1"
PORT = 8000  # Thiết lập post lắng nghe
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cấu hình kết nối
s.bind((IP, PORT))  # lắng nghe
s.listen(3)  # thiết lập tối ta 1 kết nối đồng thời
conn, addr = s.accept()  # chấp nhận kết nối và trả về thông số


value = [('accA', 1500), ('accB', 500), ('accC', 750), ('accD', 2000)]
info = dict(value)
with conn:
    try:
        # in ra thông địa chỉ của client
        print('Connected by', addr)
        while True:
            # Đọc nội dung client gửi đến
            cmd = conn.recv(1024).decode()
            # cmd = data.decode()
            if cmd == 'END':  # nếu không còn data thì dừng đọc
                print("Client disconnected!\n")
                break
            if cmd.find("getDB") == -1:  # get data from DB
                # name = cmd[7:10]
                rs = cnt.get_by_acc(cmd[7:10])
                if not rs:
                    conn.sendall('Account do not exist!'.encode())
                else:
                    for x in rs:
                        conn.sendall(str(s).encode())
                    print("Done!!!\n")
            if cmd == 'Error':  # nếu không còn data thì dừng đọc
                conn.sendall('Syntax error!! Try again.'.encode())
            if len(cmd) == 2:
                infoAcc = getAcc(cmd[1])
                if infoAcc not in info.keys():
                    conn.sendall('Account do not exist!'.encode())
                else:
                    conn.sendall(str(info.get(infoAcc)).encode())
            else:
                infoAcc = getAcc(cmd[1])
                if infoAcc not in info.keys():
                    conn.sendall('Account do not exist!'.encode())
                else:
                    money = int(cmd[2:])
                    info[infoAcc] += money
                    conn.sendall('Transaction completed!'.encode())
            # In ra Nội dung
            print('Client: ', cmd)

    finally:
        s.close()  # đóng socket
