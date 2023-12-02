def menu():
    print('======================')
    print('=====MENU PROGRAM=====')
    print('======================')
    print('1. List')
    print('2. Dictionary')
    print('3. Exit')

    pil= int(input('Pilih menu: ')) 
    print('-----------------------------')

    if pil == 1:
        list() 
        menu ()
    elif pil == 2: 
        dictionary()
        menu () 
    elif pil == 3: 
        print('Terima kasih sudah mau belajar :)')
    else:
        print('Maaf, menu tidak tersedia') 
        menu()

def list():
    car= ['AVENTADOR', 'AUDI R8', 'BMW I8'] 
    print('Daftar Mobil')
    print('1. ' + car[0])
    print('2. ' + car[1])
    print('3. ' + car[2])
    pil= int(input('Pilih mobil: '))
    if pil == 1: 
        print('Anda memilih', car[0])
    elif pil == 2:
        print('Anda memilih', car[1]) 
    elif pil == 3:
        print('Anda memilih', car[2])
    else:
        print('Maaf, mobil tidak tersedia')

def dictionary():
    fruits = {'Apel':2, 'Jeruk':3, 'Anggur':4, 'Pisang':5, 'Semangka':6}
    print('=================')
    print('TOKO BUAH BAMBANG')
    print('=================')
    print('1. Apel $2')
    print('2. Jeruk $3')
    print('3. Anggur $4') 
    print('4. Pisang $5')
    print('5. Semangka $6')
    print('=================')

    uang = int (input('Masukkan uang anda $: ')) 
    print('---------------------------')
    for i in fruits:
        print('Mau beli', i)
        jumlah = int(input('Masukkan jumlah barang: '))
        total = jumlah * fruits[i] 
        if total > uang:
            print('Uang anda tidak cukup')
            break 
        else:
            print('Total harga $'+ str(total))
            uang = uang - total 
            print('Uang anda sisa $'+ str(uang))
            print('=================')
    print('Pastikan anda menerima kembalian $'+ str(uang)) 
    print('Terima kasih sudah berbelanja :)')

menu ()