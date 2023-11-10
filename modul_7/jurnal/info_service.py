# librar bawaan python untuk tipe data
from typing import Optional, Callable, Any
from functools import wraps
import requests
from fastapi import FastAPI, Header, Response  # library fast api
# library untuk mengambil status
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()  # deklarasi objek Fast APi

LOGIN_ENDPOINT = "http://127.0.0.1:8001/login/"  # url hit API Login


class Auth(BaseModel):
    nama: str
    nim: str
    kelas: str


def auth_required(func: Callable) -> Callable:
    """
    fungsi yang mempunyai parameter fungsi lainya dan mengembalikan 
    nilai dari fungsi yang lainnya tersebut
    """
    @wraps(func)  # dekorator yang akan membuat fungsi dalam func bisa dipakai sebagai dekorator
    def wrapper(*args: Any, **kwargs: Any):
        """
        Fungsi yang akan digunaka untuk dekorator yang dimana
        menghit API dari login dan mendpatkan response jika 
        tidak terdapat HTTP error maka akan mengembalikan status dari response
        API yang di hit, jika error maka akan mengembalikan status_code dari 
        error tersebut
        """
        try:
            response = requests.post(
                url=LOGIN_ENDPOINT, json=kwargs["data"].dict(), headers={
                    "Authorization": kwargs["authorization"],
                },
            )
            response.raise_for_status()
            return func(*args, **kwargs)
        except requests.HTTPError as error:
            return Response(
                status_code=error.response.status_code
            )
    return wrapper


@app.get("/info")  # Url API dengan method get
@auth_required  # dekorator yang dibuat bahwa fungsi dibawah dekorator ini membutuhkan authentikasi jika dipergunakan
def get_information(
    data: Auth, authorization: Optional[str] = Header(None)
) -> JSONResponse:
    """
    fungsi yang mengembalikan JSON response berisi info:42
    """
    print(data)
    konten = [
        {
            'id': 1,
            'question': 'Apa yang dimaksud REST API ?'
        },
        {
            'id': 2,
            'question': "bagaimana cara kerja microservice ?"
        },
        {
            'id': 3,
            'question': "Apa perbedaan microservice dan SOA ?"
        },
        {
            'id': 4,
            'question': "kapan lebih baik menggunakan microservice ?"
        },
        {
            'id': 5,
            'question': "APa kekurangan microservice ?"
        }
    ]
    return JSONResponse(content=konten)
