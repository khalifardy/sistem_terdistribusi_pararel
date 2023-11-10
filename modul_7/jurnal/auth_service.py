from typing import Optional  # librar bawaan python untuk tipe data

from fastapi import FastAPI, Header, Response  # library fast api
# library untuk mengambil status
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from pydantic import BaseModel

app = FastAPI()  # deklarasi objek Fast APi

# end point "/login" yang direquest dengan method post dimana fungsi yang dipanggil ada dibawah dekorator ini


class Auth(BaseModel):
    nama: str
    nim: str
    kelas: str


@app.post("/login")
def login(data: Auth, authorization: Optional[str] = Header(None)) -> Response:
    """
    fungsi login dengan parameter authorization dengan nilai default None 
    mengembalikan response dengan status_code 200 OK jika authorization == sisterpar20023
    jika tidak maka akan mengembalikan response 401 UnAUTHORIZED
    """

    print(data)
    if authorization != "sisterpar2023" and data.nama != "khalifardy" and data.nim != '1304211035' and data.kelas != 'ifpjj':
        return Response(status_code=HTTP_401_UNAUTHORIZED)
    return Response(status_code=HTTP_200_OK)
