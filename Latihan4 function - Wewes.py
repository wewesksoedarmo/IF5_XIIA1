print("--------------------Program Kasir Sederhana---------------------")
pembeli = input("Masukkan nama Pembeli = ")

count = 1
print("\n--------------Menu Makanan--------------")
listmkn = ['Nasi Goreng - Rp.15000', 'Soto - Rp.9000', 'Mie Ayam - Rp.11000']
for menu in listmkn:
    print(count, '.', menu)
    count += 1

def fungsimakanan():
    global totalmkn
    global porsi
    global mkn
    nomor = int(input("\nMasukkan Pilihan [1-3] = "))
    porsi = int(input("Jumlah Pesanan = "))
    if nomor == 1:
        totalmkn = porsi * 15000
        print(porsi, "porsi Nasi Goreng Telur = Rp.", totalmkn)
        mkn = ('Nasi Goreng')
    elif nomor == 2:
        totalmkn = porsi * 9000
        print(porsi, "porsi Soto = Rp.", totalmkn)
        mkn = ('Soto')
    elif nomor == 3:
        totalmkn = porsi * 11000
        print(porsi, "porsi Mie Ayam = Rp.", totalmkn)
        mkn = ('Mie Ayam')
    else:
        print('Pilihan Tidak ada')
        fungsimakanan()
def tmbh():
    tambah = str(input("Tambah Pesanan? [Iya/Tidak] = "))
    if tambah == "Iya":
        fungsimakanan()
        totalmkn = totalmkn2
    elif tambah == "Tidak":
        totalmkn2 = 0

def minuman():
    count = 1
    print("\n--------------Menu Minuman--------------")
    listmnm = ['Es Teh - Rp.2000', 'Es Jeruk - Rp.3500', 'Es Kopi - Rp.4000']
    for menu in listmnm:
        print(count, '.', menu)
        count += 1
    def fungsiminuman():
        global totalmnm
        global gelas
        global mnm
        nomor = int(input("\nMasukkan Pilihan [1-3] = "))
        gelas = int(input("Jumlah Pesanan = "))
        if nomor == 1:
            totalmnm = gelas * 2000
            print(gelas, "gelas Es Teh = Rp.", totalmnm)
            mnm = ('Es Teh')
        elif nomor == 2:
            totalmnm = gelas * 3500
            print(gelas, "gelas Es Jeruk = Rp.", totalmnm)
            mnm = ('Es Jeruk')
        elif nomor == 3:
            totalmnm = gelas * 4000
            print(gelas, "gelas Es Kopi = Rp.", totalmnm)
            mnm = ('Es Kopi')
        else:
            print('Pilihan Tidak ada')
            fungsiminuman()
    fungsiminuman()

fungsimakanan()
tmbhmnm = str(input("Tambah Minuman? [Iya/Tidak] = "))
if tmbhmnm == "Iya":
    minuman()
elif tmbhmnm == "Tidak":
    totalmnm = 0
else:
    print("Error")
    tmbhmnm()

ttl = int(totalmkn) + int(totalmnm)
print("\nTotal Belanja Kamu = Rp.",  ttl)
uang = int(input("Uang Tunai Pembali = Rp. "))
kembalian = int(uang - ttl)
while kembalian < 0:
    uang = int(input("Input ulang uang bayar = Rp."))
    kembalian = int(uang - ttl)
print("Kembalian = Rp.", kembalian)

print("\n========================================")
print("========= S T R U K   B E L I ==========")
print("========================================")
print("Nama\t\t: ", pembeli)
print("Pesanan\t\t: ", porsi, mkn, "(Rp.", totalmkn,")")
if tmbhmnm == "Iya":
    print("\t\t\t  ", gelas, mnm, "(Rp.", totalmnm,")")
else:
    pass
print("Tagihan\t\t: Rp.", ttl)
print("Dibayar\t\t: Rp.", uang)
print("Kembalian\t: Rp.", kembalian)
print("========================================")
print("========================================")


