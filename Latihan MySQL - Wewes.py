#Download XAMMP
#Start Apache & MySQL
#Check on http://localhost/phpmyadmin/
#Check on python
#--> Setting --> Python Interpreter, kalau udh ada mysql-connector-python berarti udh connect

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
