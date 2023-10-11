import mysql.connector
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_karan'
)

cursors = db.cursor()

#Tabel 1
cursors.execute(
    """
    CREATE TABLE siswa(
    nis INT(20) NOT NULL,
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
data = [(20219001, "1563048", "Karania Arnasati", "P", '2006-4-22', "XII MIPA 1", 1),
        (20219002, "3154667", "Meyriska Anggita Putri", "P", '2006-5-3', "XII MIPA 1", 1),
        (20219003, "2450991", "Shintia Ramadhani", "P", '2006-10-22', "XII MIPA 1", 0),
        (20219004, "1133577", "Syifa Rizqya Mulyana", "P", '2006-1-22', "XII MIPA 1", 1),
        (20219005, "1308001", "Na Jaemin", "L", '2006-8-13', "XII MIPA 1", 0),
        (20219006, "2304001", "Lee Jeno", "L", '2006-4-23', "XII MIPA 1", 0),
        (20219007, "5502021", "Park Jisung", "L", '2006-2-5', "XII MIPA 1", 0),
        (20219008, "2312061", "Sheryl Callista", "P", '2006-12-23', "XII MIPA 8", 1),
        (20219009, "7211061", "Mona Sribuna", "P", '2006-11-7', "XII MIPA 7", 0),
        (20219010, "2218991", "Mark Lee", "L", '2006-8-6', "XII MIPA 4", 1)
       ]

cursors.executemany(query, data)
db.commit()

#Tabel 2
cursors.execute(
    """
    CREATE TABLE nilai_siswa(
    nis INT(20) NOTNULL,
    nama_siswa VARCHAR(30) NOT NULL,
    matematika INT(5) NOT NULL,
    bhs_inggris INT(5) NOT NULL,
    informatika INT(5) NOT NULL,
    ipa INT(5) NOT NULL,
    bhs_indonesia INT(5) NOT NULL
    )
    """
)
query1 = "INSERT INTO nilai_siswa(nis, nama_siswa, matematika, bhs_inggris, informatika, ipa, bhs_indonesia) VALUES (%s, %s, %s, %s, %s, %s, %s)"
data1 = [(20219001, "Karania Arnasati", 95, 81, 100, 92, 88),
        (20219002, "Meyriska Anggita Putri", 100, 100, 100, 100, 99),
        (20219003, "Shintia Ramadhani", 98, 100, 86, 78, 90),
        (20219004, "Syifa Rizqya Mulyana", 95, 88, 79, 91, 100),
        (20219005, "Na Jaemin", 94, 95, 96, 97, 98),
        (20219006, "Lee Jeno", 99, 100, 100, 100, 100),
        (20219007, "Park Jisung", 82, 94, 87, 85, 77),
        (20219008, "Sheryl Callista", 93, 97, 89, 90, 100),
        (20219009, "Mona Sribuna", 81, 85, 83, 90, 87),
        (20219010, "Mark Lee", 91, 93, 100, 88, 90)
       ]
cursors.executemany(query1, data1)
db.commit()
