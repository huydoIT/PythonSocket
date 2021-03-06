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
            name = str(getAcc(cmd[1]))
            print(name)
            db = cnt.get_by_acc(name)
            if not db:
                conn.sendall('Account do not exist!'.encode())
            else:
                if cmd[0] == 'R':  # check message
                    conn.sendall(str(db[0]).encode())
                    # print("Done!!!") Test
                else:
                    balance = int(db[0]) + int(cmd[2:])
                    if balance < 0:
                        conn.sendall('Balance not enough!'.encode())
                    else:
                        if cnt.update_data((balance, name)) == 1:
                            db = cnt.get_by_acc(name)
                            conn.sendall(str(db[0]).encode())
                        else:
                            conn.sendall('Update failed!'.encode())
                        # conn.sendall('Transaction completed!'.encode())
            # In ra Nội dung
            print('Client: ', cmd)

    finally:
        s.close()  # đóng socket
