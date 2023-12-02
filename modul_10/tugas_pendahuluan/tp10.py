import threading


def cek_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def hitung_prima(start, end, hasil):
    total = 0
    for bil in range(start, end+1):
        if cek_prima(bil):
            total += 1
    hasil.append(total)


inpt = input("masukan rentang (ex:2,10) : ")
lst = inpt.split(",")
jumlah_thread = 10
hasil_ = []
part = (int(lst[1])-int(lst[0]))//jumlah_thread

threads = []

for i in range(jumlah_thread+1):
    start = i * part
    end = (i + 1) * part if i < jumlah_thread else int(lst[1])-int(lst[0])
    thread = threading.Thread(target=hitung_prima, args=(start, end, hasil_))
    threads.append(thread)
    thread.start()

print(f"hasil bilangan prima {sum(hasil_)}")
