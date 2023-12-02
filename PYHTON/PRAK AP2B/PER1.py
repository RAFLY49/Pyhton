print('-------------------------------')
print('         Konversi Suhu         ')
print('-------------------------------')
hari = input('Hari apa ini? ')
cel = int(input('Masukkan Suhu dalam Celcius: '))
print('-------------------------------')

reamur = 4/5 * cel
fah = (9/5 * cel) + 32
kelvin = cel + 273

print('Hari', hari, 'Suhu dalam Celcius: %.0f' % cel+'°')
print('Hari', hari, 'Suhu dalam Reamur: %.0f' % reamur+'°')
print('Hari', hari, 'Suhu dalam Fahrenheit: %.0f' % fah+'°')
print('Hari', hari, 'Suhu dalam Kelvin: %.0f' % kelvin+'°')