menu_minum = ['Kopi Hideung', 'Kopi Moccha', 'Kopi Latte', 'Ice Americano']
count = 1

print('==============================')
print('-----CAFE KOPRAL SUHERMAN-----')
print('++++++++++++++++++++++++++++++')

print(str('Daftar Menu'))
for menu in menu_minum:
    print(count,'.', menu)
    count += 1
nm_order=str(input('Nama pemesan = '))
plh=int(input('Pilihan [1-4] = '))
if plh == 1:
    mn = menu_minum[0]
    hrg = 12000
elif plh == 2:
    mn = menu_minum[1]
    hrg = 12500
elif plh == 3:
    mn = menu_minum[2]
    hrg = 13000
elif plh == 4:
    mn = menu_minum[3]
    hrg = 15000
else:
    print('Pilihan tidak terdaftar')

if plh >= 1 and plh <=4:
    print('Menu yang anda pilih', mn)
    print('Harga = ', hrg)
    qty=int(input('Jumlah = '))
    ttl=int(qty)*int(hrg)
    print('Total belanja anda Rp', ttl)
    byr=int(input('Input Nominal Pembayaran = '))
    kmbln=int(byr)-int(ttl)
    while kmbln < 0:
            krg = int(ttl)-int(byr)
            print('Uang anda kurang', krg)
            byr=int(input('Input Ulang Nominal Pembayaran = '))
    if kmbln == 0:
        pass
    elif kmbln > 0:
        print('Kembalian anda Rp', kmbln)

print('Terimakasih', nm_order, 'telah berbelanja')