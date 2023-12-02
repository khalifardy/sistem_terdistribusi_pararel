import threading


def perkalian(n):
    total = None
    for num in range(1, n+1):
        if total == None:
            total = num
        else:
            total *= num
    return total


def faktorial(n, hasil):
    total = None
    for bil in range(1, n+1):
        if total == None:
            total = bil
        else:
            total *= bil
    hasil.append(total)


inpt = input("masukan faktorial n,m (ex:2,10) : ")
lst = inpt.split(",")
jumlah_thread = 2
hasil_ = []
part = (int(lst[1])-int(lst[0]))//jumlah_thread

threads = []

for i in lst:
    thread = threading.Thread(target=faktorial, args=(int(i), hasil_))
    threads.append(thread)
    thread.start()

print(f"faktorial {lst[0]} : {hasil_[0]}")
print(f"faktorial {lst[1]} : {hasil_[1]}")
