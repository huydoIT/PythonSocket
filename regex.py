import re

while True:
    s = input("Input string: ")
    if s == "END":
        print("Exit")
        break
    match = re.match(r'[a,b,c]+', s)
    # match = re.search(r'^h', str)
    if match:  # nếu tồn tại chuỗi khớp
        print("OK!")
    else:
        print("Not exits!")
