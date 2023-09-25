from library_TP2 import KalkulatorSederhana

def input_angka():
    while True:
        try:
            angka1 = int(input("Masukan angka pertama: "))
            angka2 = int(input("Masukan angka kedua: "))
            break
        except:
            print("masukan hanya angka \n")
    
    return angka1,angka2

def menu():
    while True:
        try:
            operator = int(input())
            if operator not in [1,2,3,4,5]:
                print("masukan hanya angka 1-5")
            else:
                break
                
        except:
            print("hanya masukan angka 1-5")
    
    return operator

def pilih_operas1(angka):
    print(f"pilih operasi: {angka}")


def main():
    print(
        "Kalkulator Sederhana \n",
        "===================== \n",
        "NAMA: Khalifardy Miqdarsah \n",
        "NIM : 1304211035 \n",
        "KELAS : IF-45-01.1PJJ \n",
        "====================== \n"
    )
    

    while True:
        
        angka1,angka2 = input_angka()
        mat = KalkulatorSederhana(angka1,angka2)

        print(
           "Operasi \n",
           "1. Tambah \n",
           "2. Kurang \n",
           "3. Kali \n",
           "4. Bagi \n"
           "5. Exit \n"
        )
        operator = menu()
        pilih_operas1(operator)

        if operator == 1:
            print(f"Hasil Penjumlahan: {mat.tambah()}")
        elif operator ==2:
            print(f"Hasil Pengurangan: {mat.kurang()}")
        elif operator == 3:
            print(f"Hasil Perkalian: {mat.kali()}")
        elif operator == 4:
            print(f"Hasil Pembagian: {mat.bagi()}")
        elif operator == 5:
            print("exit program")
            break

        print("\n")
        ex = input("Apakah masih melanjutkan menghitung  ? (Y/y N/n) : ")

        if ex in ["N","n"]:
            print("exit program")
            break


if __name__ :
    main()


        




            
    