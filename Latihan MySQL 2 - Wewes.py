import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database = 'db_wewes'
)

cursors = db.cursor()

#Syntax Membuat Database
#Jika database sudah terbuat, maka program di bawah tidak dapat dijalankan
#Buat database baru dengan mengganti "db_wewes" dengan nama database baru
cursors.execute("CREATE DATABASE db_wewes")

#Syntax Membuat Tabel
#Jika tabel sudah terbuat, maka program di bawah tidak dapat dijalankan
#Buat tabel baru dengan mengganti "user" dengan judul tabel baru
cursors.execute(
    """
    CREATE TABLE user(
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL
    )
    """
)



