def greet():
    print('Halo Dunia')
    kabar = input(str('Apa Kabar Kamu? '))
    nm = input(str('Nama Kamu Siapa? '))
    print('Halo', nm, 'Kamu', kabar, 'Saja ya' )

x = 50
def fungsi(x):
    print('x = ', x)
    x = 2
    print ('merubah lokal variabel x = ', x)

fungsi(100)
print(x)


def katakan(pesan, jumlah=1):
    print (pesan * jumlah)

katakan('Halo ')
katakan('Halo ', 3)


def fungsi(a, b=5, c=10):
    print
    'a = ', a
    print
    'b = ', b
    print
    'c = ', c

fungsi(3, 7)
fungsi(25, c=24)
fungsi(c=50, a=100)