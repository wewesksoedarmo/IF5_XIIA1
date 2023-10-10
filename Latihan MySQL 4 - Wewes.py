import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_karan'
)

cursors = db.cursor()
#Tabel 1
cursors.execute("CREATE DATABASE db_wewes")
cursors.execute(
    """
    CREATE TABLE siswa(
    nis INT AUTO_INCREMENT PRIMARY KEY,
    nisn VARCHAR(10) NOT NULL,
    nama_siswa VARCHAR(30) NOT NULL,
    jenis_kelamin VARCHAR(4) NOT NULL,
    tanggal_lahir date NOT NULL,
    kelas VARCHAR(20) NOT NULL,
    status INT(4) NOT NULL
    )
    """
)
query = "INSERT INTO siswa(nis, nisn, nama_siswa, jenis_kelamin, tanggal_lahir, kelas, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
data = [("", "1563048", "Karania Arnasati", "P", '2006-4-22', "XII MIPA 1", 1),
        ("", "3154667", "Meyriska Anggita Putri", "P", '2006-5-3', "XII MIPA 1", 1),
        ("", "2450991", "Shintia Ramadhani", "P", '2006-10-22', "XII MIPA 1", 0),
        ("", "1133577", "Syifa Rizqya Mulyana", "P", '2006-1-22', "XII MIPA 1", 1),
        ("", "1308001", "Na Jaemin", "L", '2006-8-13', "XII MIPA 1", 0),
        ("", "2304001", "Lee Jeno", "L", '2006-4-23', "XII MIPA 1", 0),
        ("", "5502021", "Park Jisung", "L", '2006-2-5', "XII MIPA 1", 0),
        ("", "2312061", "Sheryl Callista", "P", '2006-12-23', "XII MIPA 8", 1),
        ("", "7211061", "Mona Sribuna", "P", '2006-11-7', "XII MIPA 7", 0),
        ("", "2218991", "Mark Lee", "L", '2006-8-6', "XII MIPA 4", 1)
       ]

cursors.executemany(query, data)
db.commit()
