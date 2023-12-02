class bangundatar:
    def persegi (self, sisi):
        luas = sisi ** 2 
        return luas
    def lingkaran (self, jari): 
        luas = 22/7 * jari ** 2
        return luas
    def segitiga (self, alas, tinggi):
        luas = 0.5 * alas * tinggi
        return luas

def menu():
    objek = bangundatar ()
    print('----------------') 
    print('Program Luas Bangun Datar')
    print('----------------')
    print('1. Persegi\n2. Lingkaran\n3. Segitiga\n4. Keluar') 
    pilih= int(input('Pilih Menu : '))
    if pilih== 1:
        sisi = int(input('Masukkan Sisi : '))
        print('Luas Persegi: ', objek.persegi (sisi))
        kembali()
    elif pilih == 2:
        jari = int(input('Masukkan Jari-Jari: '))
        print('Luas Lingkaran: ', objek.lingkaran(jari))
        kembali()
    elif pilih == 3:
        alas = int(input('Masukkan Alas: '))
        tinggi = int(input('Masukkan Tinggi : '))
        print('Luas Segitiga; ', objek.segitiga(alas, tinggi))
        kembali() 
    elif pilih == 4:
        print('Terima Kasih Sudah Mau Belajar :)')
        exit() 
    else:
        print('Pilihan tidak ada')
        kembali()

def kembali(): 
    kembali = input('Kembali ke menu (Y/T): ')
    if kembali == 'Y' or kembali == 'y': 
        menu()
    else:
        print('Terima Kasih Sudah Mau Belajar :)')
        exit()

menu ()