import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_wewes'
)

cursors = db.cursor()

sql = "UPDATE siswa SET nama_siswa =%s WHERE nama_siswa=%s"
data = "Wewes K Soedarmo", "Karania Arnasati"
cursors.execute(sql,data)
db.commit()

