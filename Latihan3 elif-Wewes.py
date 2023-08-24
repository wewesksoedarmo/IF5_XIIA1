no1 = 'Kopi Hideung'
no2 = 'Kopi Mocca'
no3 = 'Kopi Latte'
no4 = 'Kopi Ciwidey'
hrg1 = '7000'
hrg2 = '8500'
hrg3 = '7500'
hrg4 = '9000'

print('==============================')
print('-----CAFE KOPRAL SUHERMAN-----')
print('++++++++++++++++++++++++++++++')

print('~~MENU~~')
print('1.', no1)
print('2.', no2)
print('3.', no3)
print('4.', no4)
print('++++++++++++++++++++++++++++++')

nm_order=str(input('Nama pemesan = '))
plh=int(input('Pilihan [1-4] = '))
if plh == 1:
    print('Minuman Pesanan Kamu', no1)
    print('Harga Per Cup Rp', hrg1)
    qty=input('Berapa Cup Order = ')
    ttl_hrg = int(qty) * int(hrg1)
elif plh == 2:
    print('Minuman Pesanan Kamu', no2)
    print('Harga Per Cup Rp', hrg2)
    qty=input('Berapa Cup Order = ')
    ttl_hrg = int(qty) * int(hrg2)
elif plh == 3:
    print('Minuman Pesanan Kamu', no3)
    print('Harga Per Cup Rp', hrg3)
    qty=input('Berapa Cup Order = ')
    ttl_hrg = int(qty) * int(hrg3)
elif plh == 4:
    print('Minuman Pesanan Kamu', no4)
    print('Harga Per Cup Rp', hrg4)
    qty=input('Berapa Cup Order = ')
    ttl_hrg = int(qty) * int(hrg4)
else:
    print('Menu Tidak Ditemukan')

adm = str(input('Tambah Pesanan? (Iya/Tidak) '))
if adm == 'Tidak':
    pass
elif adm == 'Iya':
    print('bntr blm kubikin')

print('Total Pesanan Kamu Rp.', ttl_hrg)
byr = int(input('Uang Pembayaran Kamu Rp.'))
if byr > ttl_hrg:
    kmbln = int(byr) - int(ttl_hrg)
    print('Kembalian Rp.', kmbln)
elif byr < ttl_hrg:
    krg = int(ttl_hrg) - int(byr)
    print('Uang Kamu Kurang Rp.', krg)
elif byr == ttl_hrg:
    print('Terimakasih Telah Berbelanja')
else:
    print('Error')