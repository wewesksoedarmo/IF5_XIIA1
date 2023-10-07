import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_wewes'
)

cursors= db.cursor()

sql = "INSERT INTO user(id, firstname, lastname, username, password) VALUES (%s, %s, %s, %s, %s)"
val = [("", "Karania", "Arnasati", "weweschaf", "mcchickendoublenuggets"),
       ("", "Banu", "Saptono", "lord_bbaneu", "yuni220679")
       ]
cursors.executemany(sql, val)
db.commit()
print("data berhasil direkam")