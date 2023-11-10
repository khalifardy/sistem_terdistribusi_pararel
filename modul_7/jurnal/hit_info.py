import requests
import json

headers = {
    'authorization': "sisterpar2023"
}

data = {
    'nama': "khalifardy",
    'nim': "1304211035",
    'kelas': "ifpjj"
}

r = requests.get("http://127.0.0.1:8000/info", headers=headers, json=data)

print(r.json())
