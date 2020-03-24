import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="acc_db")
cur = conn.cursor()


def get_data():
    try:
        sql = "SELECT * FROM account"
        cur.execute(sql)
        rs = cur.fetchall()
        if not rs:
            print("Data empty!\n")
        else:
            print("=== Account info ===")
            print("ID\tAccount\tBalance")
            for row in rs:
                print("%s\t%s\t%d" % (row[0], row[1], row[2]))
            print("====================")
    except:
        conn.rollback()


def get_by_acc(acc):
    try:
        sql = "SELECT balance FROM account WHERE acc =%s"

        cur.execute(sql, (acc,))
        rs = cur.fetchone()
        if not rs:
            return None
        else:
            return rs
    except:
        conn.rollback()


def get_test():
    try:
        sql = "SELECT * FROM account"
        cur.execute(sql)
        rs = cur.fetchall()
        if not rs:
            return None
        else:
            return rs
    except:
        conn.rollback()


def update_data(value):
    try:
        sql = "UPDATE `account` SET `balance`=%s WHERE `acc`=%s"
        # adr = tuple()  # ("accB", )
        cur.execute(sql, value)
        conn.commit()
        return 1
    except:
        conn.rollback()
        return 0
