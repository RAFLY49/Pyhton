array_data = []
while True:
    nama = input("Masukan Nama : ")
    umur = input("Masukan Umur : ")
    aray_dataBaru = [nama, umur]
    array_data.append(aray_dataBaru)
    user = input("Ketik Y untuk lanjut, Ketik STOP untuk menghentikan Program (Y/STOP)? ")
    user not in ["Y","STOP"]

    if user == "STOP":
        print("Program berhenti")
        break

print("======================================")
for i,data in enumerate(array_data):
    print(f"Saya {data[0]}, {data[1]} Tahun")