class Siswa:
    # variable class/ class variable
    jumlah = 0

    # init dieksekusi saat init dibuat
    # __init__ / initialisiation / inisialisasi
    def __init__(self, inputNim, inputNama):
        # instance variabel
        self.nim = inputNim
        self.nama = inputNama
        Siswa.jumlah += 1
        print('berhasil menambah siswa, dengan nama', self.nama)


s1 = Siswa(113001, 'Andi Surandi')
s2 = Siswa(113002, 'Otong Maman')

print(s1.__dict__)
print(s2.__dict__)
print(Siswa.__dict__)
