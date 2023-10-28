import requests
import json

# Note :
# Daftar/login menggunakan list email berikut atau register akan failed:
# george.bluth@reqres.in, janet.weaver@reqres.in, emma.wong@reqres.in, eve.holt@reqres.in, charles.morris@reqres.in
# tracey.ramos@reqres.in, michael.lawson@reqres.in, lindsay.ferguson@reqres.in, tobias.funke@reqres.in, byron.fields@reqres.in
# george.edwards@reqres.in, rachel.howell@reqres.in
# ----------------------------------
# GUNAKAN NIM ANDA SEBAGAI PASSWORD
# ----------------------------------


def display_user():  # (15)
    # I.S -
    # F.S Menampilkan seluruh data user dalam bentuk list yang diiterasi
    r = requests.get("https://reqres.in/api/unknown")
    resp = r.json()
    page = resp['total_pages']

    pages = 0
    list_data = []
    for i in range(page):
        url = f"https://reqres.in/api/users?page={i+1}"
        hit = requests.get(url)

        list_data.append(hit.json()["data"])

    for i in list_data:
        for j in i:
            print(
                "---------------------------------------\n",
                f"ID user : {j['id']}\n E-Mail Users : {j['email']}\n Name : {j['first_name']} {j['last_name']}"
            )


def get_user(id):  # (10)
    # I.S id user yang akan ditampilkan
    # F.S Menampilkan data satu user yang diminta, dan print "Data tidak ditemukan" apabila user tidak ditemukan
    url = f"https://reqres.in/api/users/{id}"
    r = requests.get(url)
    res = r.json()

    if len(res) > 0:
        resp = res['data']

        print(
            "---------------------------------------\n",
            f"ID user : {resp['id']}\n E-Mail Users : {resp['email']}\n Name : {resp['first_name']} {resp['last_name']}"
        )
    else:
        print("Data tidak ditemukan")


def register(email, password) -> int:  # (15)
    # I.S email dan password yang akan diregister
    # F.S kode status response apabila user sukses diregister (200 / HTTP OK)
    url = "https://reqres.in/api/register"
    data = {
        "email": f"{email}",
        "password": f"{password}"
    }

    r = requests.post(url, json=data)
    print(r.json())

    if r.status_code == 200:
        return 200
    else:
        return 400


def login(email, password) -> int:  # (15)
    # I.S email dan password yang akan login
    # F.S kode status response apabila user sukses login (200 / HTTP OK)
    url = "https://reqres.in/api/login"
    data = {
        "email": f"{email}",
        "password": f"{password}"
    }
    r = requests.post(url, json=data)

    if r.status_code == 200:
        return 200
    else:
        return 400


def edit_user(name):  # (15)
    # I.S nama user baru untuk user yang login
    # F.S tampilkan "Sukses edit!" apabila edit nama berhasil (200 / HTTP OK), atau print error jika tidak
    url = "https://reqres.in/api/users/1"
    data = {
        "name": f"{name}"
    }
    resp = requests.patch(url, json=data)
    if resp.status_code == 200:
        print("Sukses edit")
    else:
        print("error")


def delete_user(id):  # (15)
    # I.S id user yang akan dihapus (1 - 12)
    # F.S tampilkan "Sukses terhapus!" apabila data sukses terhapus (204 / HTTP NO CONTENT), atau print error jika tidak
    url = f"https://reqres.in/api/users/{id}"
    resp = requests.delete(url)
    if resp.status_code == 204:
        # Print sukses
        print("Sukses terhapus!")
    else:
        print("error")


def show_menu():  # (5)
    # I.S -
    # F.S tampilkan menu sederhana untuk menampilkan pilihan yang bisa dilakukan user
    choose = 1
    while 1 <= choose <= 4:
        print("Menu admin sederhana")
        print("---------------------------------------")
        print("1. Tampilkan Semua User")
        print("2. Tampilkan Satu User")
        print("3. Ubah Nama Anda")
        print("4. Hapus User")
        print("---------------------------------------")
        choose = int(input("Masukkan pilihan anda: "))
        if choose == 1:
            print("Menampilkan data User")
            display_user()
        elif choose == 2:
            id_input = input("Masukkan id user yang ingin ditampilkan: ")
            # Jalankan fungsi get user
            print(f"Menampilkan Data User dengan ID : {id_input}")
            get_user(id_input)
        elif choose == 3:
            new_name = input("Masukkan nama baru: ")
            # Jalankan fungsi edit user
            edit_user(new_name)
        elif choose == 4:
            del_user = input("Masukkan id user yang akan dihapus: ")
            # Jalankan fungsi delete user
            delete_user(del_user)
        else:
            print("Keluar dari aplikasi...")


def login_menu():  # (5)
    # I.S -
    # F.S tampilkan input sederhana untuk input email dan password untuk masuk kedalam aplikasi
    success = False
    while not success:
        print("Masuk ke reqres")
        print("---------------------------------------")
        email = input("Email : ")
        password = input("Password : ")
        check = login(email, password)
        salah = False
        if check == 400:
            salah = True
        # Jalankan fungsi login
        if salah:
            print("Masukkan password dan gunakan email yang sudah terdaftar")
        else:
            print("Login sukses!")
            success = True
            show_menu()


def register_menu():  # (5)
    # I.S -
    # F.S tampilkan input sederhana untuk input email dan password untuk register kedalam aplikasi
    success = False
    while not success:
        print("Daftar ke reqres")
        print("---------------------------------------")
        email = input("Email : ")
        password = input("Password : ")
        check = register(email, password)
        salah = False
        if check == 400:
            salah = True

        # Jalankan fungsi register
        if salah:
            print("Masukkan password dan gunakan email yang sudah terdaftar")
        else:
            print("Login sukses!")
            success = True
            show_menu()


def main_menu():
    print("Praktikum HTTP API")
    print("NAMA : Khalifardy Miqdarsah")
    print("NIM  : 1304211035")
    print("---------------------------------------")
    print("1. Login")
    print("2. Register")
    print("---------------------------------------")
    pilihan = int(input("Masukkan pilihan anda : "))
    if pilihan == 1:
        login_menu()
    else:
        register_menu()


main_menu()
