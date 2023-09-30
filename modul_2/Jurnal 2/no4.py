import math

def determinan(a,b,c):
    D = b**2 - (4*a*c)
    return D

masukan = input("masukan nilai a b c:")
list_angka = [int(i) for i in masukan.split()]

D = determinan(list_angka[0],list_angka[1],list_angka[2])
if D >= 0:
    x1 = (-list_angka[1] + math.sqrt(D))/(2*list_angka[0])
    x2 = (-list_angka[1] - math.sqrt(D))/(2*list_angka[0])
    print(f"x1 = {x1} dan x2 = {x2}")
else:
    D = math.sqrt(-D)
    print(
        f"x1 = -{list_angka[1]} + {D} i"
    )
    print(
        "      ----------------------"
    )
    print(
        f"               {2*list_angka[0]}"
    )
    print("\n")

    print(
        f"x2 = -{list_angka[1]} - {D} i"
    )
    print(
        "      ----------------------"
    )
    print(
        f"               {2*list_angka[0]}"
    )
