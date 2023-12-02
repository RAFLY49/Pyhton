def net():
    print('')
    print('========WELCOME TO=======')
    print('========RAF GAMING=======')
    print('==========ENJOY!=========')
    print('1. Room')
    print('2. Makanan')
    print('3. Minuman')
    print('4. Exit')

    pil = int(input('Pilih Menu: ')) 
    print('')
    if pil == 1:
        room()
        net()
    elif pil == 2: 
        MA()
    elif pil == 3: 
        MI()
    elif pil == 4: 
        print('Terima Kasih Telah Berkunjung')
        exit()
    else:
        print('Pilih Angak Yang Benar!') 
        net()

class billing:
    def VVIP (self, jam):
        bill = jam * 5
        return bill
    def VIP (self, jam): 
        bill = jam * 4
        return bill
    def reguler (self, jam):
        bill = jam * 2
        return bill

def room():
    pay = billing ()
    print('=====ROOM=====')
    print('1. VVIP')
    print('2. VIP')
    print('3. Reguler')
    print('4. Exit')
    pil = int(input('Pilih Menu : '))
    if pil == 1:
        jam = int(input('Lama Bermain: '))
        print('Tagihan $: ', pay.VVIP (jam))
        print('Selamat Bermain')
        net()
    elif pil == 2:
        jam = int(input('Lama Bermain: '))
        print('Tagihan $: ', pay.VIP (jam))
        print('Selamat Bermain')
        net()
    elif pil == 3:
        jam = int(input('Lama Bermain: '))
        print('Tagihan $: ', pay.reguler (jam))
        print('Selamat Bermain')
        net()
    elif pil == 4:
        print('Anda Akan Kembali Pada Menu Utama')
        net()
    else:
        print('Pilih Angka Yang Benar!')
        room()
    
def MA():
        food = ["Nasi Goreng","Indomie","Roti Bakar","Sosis","Baso"]
        print('')
        print('Daftar Makanan')
        print('1. ' + food[0])
        print('2. ' + food[1])
        print('3. ' + food[2])
        print('4. ' + food[3])
        print('5. ' + food[4])

        pil = int(input('Pilih Makanan: '))
        if pil == 1: 
            print('Anda Memesan', food[0])
        elif pil == 2:
            print('Anda Memesan:', food[1]) 
        elif pil == 3:
            print('Anda Memesan:', food[2])
        elif pil == 4:
            print('Anda Memesan:', food[3])
        elif pil == 5:
            print('Anda Memesan:', food[4])
        else:
            print('Makanan Yang Anda Pilih Tidak Tersedia')

        while(True):
            tanya = input("Apakah Anda Ingin Memesan lagi? y/g : ")
            if tanya == 'y':
                MA()
            if tanya == 'g':
                net()
            break
def MI():
        drink = ["Good Day Fresh","Max Tea","Kukubima","Pop Ice","Nutrisari"]
        print('')
        print('Daftar Minuman')
        print('1. ' + drink[0])
        print('2. ' + drink[1])
        print('3. ' + drink[2])
        print('4. ' + drink[3])
        print('5. ' + drink[4])

        pil = int(input('Pilih Minuman: '))
        if pil == 1: 
            print('Anda Memesan', drink[0])
        elif pil == 2:
            print('Anda Memesan:', drink[1]) 
        elif pil == 3:
            print('Anda Memesan:', drink[2])
        elif pil == 4:
            print('Anda Memesan:', drink[3])
        elif pil == 5:
            print('Anda Memesan:', drink[4])
        else:
            print('Minuman Yang Anda Pilih Tidak Tersedia')

        while(True):
            tanya = input("Apakah Anda Ingin Memesan lagi? y/g : ")
            if tanya == 'y':
                MI()
            if tanya == 'g':
                net()
            break
net()
