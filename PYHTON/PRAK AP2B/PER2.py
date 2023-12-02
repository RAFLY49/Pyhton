print('=================')
print('    TOKO BUAH    ')
print('=================')
print('1. Apel $2')
print('2. Jeruk $3')
print('3. Anggur $4')
print('4. Pisang $5')
print('5. Semangka $5')
print('=================')

uang = int(input('Masukkan uang anda $: '))
print('-------------------------')
for i in range(1,6):
    if i == 1:
        print('Mau beli Apel?')
    elif i == 2:
        print('Mau beli Jeruk?') 
    elif i == 3:
        print('Mau beli Anggur?')
    elif i == 4: 
        print('Mau beli Pisang?')
    else:
        print('Mau beli Senangka?')
    jumlah = int(input('Masukkan jumlah barang: '))
    if i == 1:
        total = jumlah * 2
    elif i == 2:
        total = jumlah * 3
    elif i == 3:
        total = jumlah * 4
    elif i == 4:
        total = jumlah * 5
    else:
        total = jumlah * 6
    if total > uang:
        print('Uang anda tidak cukup')
        break
    else:
        print('Total Harga $'+ str(total))
        uang = uang - total
        print('Uang anda sisa $'+ str(uang))
        print('==================')
print('Pastikan anda menerima kembalian $'+ str(uang))
print('Terima kasih sudah berbelanja :)')