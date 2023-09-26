import datetime
import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
)

if db.is_connected():
    print('Koneksi ke Mysql Database Berhasil')
    current_date = datetime.date.today()
    print(current_date)