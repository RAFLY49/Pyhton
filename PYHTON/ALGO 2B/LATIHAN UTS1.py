nama = input("Masukkan nama anda : ")
npm = input("Masukkan NPM anda : ")
kelas = input("Masukkan kelas anda : ")
matkul = input("Masukkan mata kuliah anda : ")
uts = int(input("Masukkan nilai UTS anda : "))
uas = int(input("Masukkan nilai UAS anda : "))
print("=======================")
total = (uts+uas)/2
if total >= 86 and total <= 100:
    grade = "A"
elif total >= 71 and total <= 85:
    grade = "B"
elif total >= 61 and total <= 70:
    grade = "C"
else:
    grade = "D"
print("Nama anda adalah "+nama)
print("NPM anda adalah "+npm)
print("Kelas anda adalah "+kelas)
print("Mata Kuliah anda adalah "+matkul)
print("Nilai total anda adalah "+str(total))
print("Grade anda adalah "+grade)