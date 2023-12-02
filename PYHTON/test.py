jenisMenu=["Makanan","Minuman","Snack"]
menuMakanan=["Nasi goreng","Nasi Pecel","Soto","Lalapan"]
menuMinuman=["Es teh","Es jeruk","Es degan","air putih"]
menuSnack=["Kuaci","Kentang goreng","Kucur","Jamur krispi"]
Total=[]

while True: 
    print("---Daftar Menu---")
    print("-----------------")
    print(" 1. | Makanan  | ")
    print(" 2. | Minuman  | ")
    print(" 3. | Snack    | ")
    print("-----------------")
    pilihMenu=(input("masukkan menuu 1-3 : "))
    if pilihMenu== "1" :
        print("anda memilih menu makanan")
        for j in range(0,len(menuMakanan)):
            print(f"{j+1} {menuMakanan[j]}")
        ulangi= True
        while ulangi:
            pilihmakanan=int(input(f"pilih menu makanan 1-4 : "))
            if pilihmakanan <=0 or pilihmakanan > len(menuMakanan):
                print("masukan menu makanan")
                for j in range(0, len(menuMakanan)):
                    print(f"{j+1} {menuMakanan[j]}")
                continue
            else:
                Total.append(menuMakanan[pilihmakanan-1])
                print("Pesanan")
                for list_total in range(0,len(Total)):
                    print(f"{list_total +1} {Total[list_total]}")
                ulangi= False
            continue
    elif pilihMenu == "2":
        print("anda memilih menu minuman")
        for minuman in range(0,len(menuMinuman)):
            print(f"{minuman+1} {menuMinuman[minuman]}")
        ulangi= True
        while ulangi:
            pilihminuman=int(input(f"pilih menu minuman 1-4"))
            if pilihminuman <=0 or pilihminuman > len(menuMinuman):
                print("masukan menu minuman")
                for minuman in range(0, len(menuMinuman)):
                    print(f"{minuman+1} {menuMakanan[minuman]}")
                continue
            else:
                Total.append(menuMinuman[pilihminuman-1])
                print("Pesanan")
                for list_total in range(0,len(Total)):
                    print(f"{list_total +1} {Total[list_total]}")
                ulangi= False
            continue
    elif pilihMenu=="3":
        print("anda memilih menu snack")
        for k in range(0,len(menuSnack)):
            print(f"{k+1} {menuSnack[k]}")
        ulangi= True
        while ulangi:
            pilihsnack=int(input(f"pilih menu snack 1-4"))
            if pilihsnack <=0 or pilihsnack > len(menuSnack):
                print("masukan menu snack")
                for k in range(0, len(menuSnack)):
                    print(f"{k+1} {menuSnack[k]}")
                continue
            else:
                Total.append(menuSnack[pilihsnack-1])
                print("Pesanan")
                for list_total in range(0,len(Total)):
                    print(f"{list_total +1} {Total[list_total]}")
                ulangi= False
    else:
        print("menu tidak ditemukan")
        continue
    tanya = ""
    while tanya != "g":
        tanya= input("apakah ada tambahan?y/g : ")
        print("====  Pesanan ====")
        for list_total in range(0, len(Total)):
            print(f"{list_total +1}  {Total[list_total]} 1x")
        break
    