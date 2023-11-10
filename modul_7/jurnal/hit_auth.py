import requests
import json

nama = input("Masukan Nama: ")
nim = input("Masukan nim: ")
kelas = input("masukan kelas: ")

header = {
    'authorization': "sisterpar2023"
}
data = {
    'nama': nama,
    'nim': nim,
    'kelas': kelas
}
payload = json.dumps(data)

r = requests.post("http://127.0.0.1:8001/login", json=data, headers=header)
if r.status_code == 200:
    print(r.status_code)
    print("Login sukses")
else:
    print(r.status_code)
    print("login gagal")
