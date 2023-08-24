count = 1
stock = ['Fiksi', 'Non Fiksi', 'Science', 'Ilmu Filsafat']

print('======================================')
print('         SEWA BUKU BUK BUKIN         ')
print('==XXXX==XXXX==XXXX==XXXX==XXXX==XXXX==')
print('STOK BUKU DISEWAKAN:')
for data in stock:
    print(count,'.', data)
    count += 1
print('======================================')

nm = str(input('Nama Peminjam = ', ))
plh = int(input('Pilihan Buku [1-4] = ', ))
if plh == 1:
    hrg = '13000'
    bk = stock[0]
elif plh == 2:
    hrg = '15000'
    bk = stock[1]
elif plh == 3:
    hrg = '12000'
    bk = stock[2]
elif plh == 4:
    hrg = '20000'
    bk = stock[3]
else:
    print('Menu yang anda pilih tidak tersedia')

if plh >= 1 and plh <= 4:
    print('Anda memilih buku =', bk)
    drs = str(input('Lama Peminjaman(hari) = ', ))
    ttl_hrg = int(hrg) * int(drs)
    print('Anda akan meminjam buku', bk, 'dengan harga Rp', hrg, 'per hari')
    print('Total Harga Rp.', ttl_hrg)
    byr = int(input('Nominal Uang Pembayaran = Rp. ', ))
    kmbln = int(byr) - int(ttl_hrg)
    while kmbln < 0:
            print('Uang anda kurang')
            byr = int(input('Input ulang nominal uang pembayaran = Rp.', ))
            kmbln = int(byr) - int(ttl_hrg)
    if kmbln == 0:
        print('Uang anda pas')
    elif kmbln > 0:
        print('Kembalian anda = Rp.', kmbln)
print('Terimakasih', nm, 'telah berkunjung')
