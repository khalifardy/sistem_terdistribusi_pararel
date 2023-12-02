import threading
import time
import math

# hasil dari setiap thread di simpan pada list global bernama my_result
# hasil perhitungan thread 1 akan disimpan pada indek 0, dst
my_result = []


# buatlah fungsi untuk menghitung pi menggunakan Riemann zeta function
# (pi^2)/6 = 1/(1^2)+ 1/(2^2) + 1/(3^2) + 1/(4^2) + ...
def calculate_pi(lower, upper, index_of_thread):
    result = 0
    for i in range(lower, upper):
        result += 1/(i**2)

    my_result.insert(index_of_thread, result)


start = time.time()
if __name__ == "__main__":
    # hitung pi dengan indek 1 - 10000
    # buatlah 5 thread yang memanggil fungsi calculate_pi
    # thread 1 : indek 1 - 2000, thread 2 2000-4000, dst
    jumlah_thread = 5
    part = 10000//jumlah_thread
    threads = []
    for i in range(jumlah_thread+1):
        lower = i * part+1
        upper = ((i + 1) * part)+1 if i < jumlah_thread else 10001
        t1 = threading.Thread(target=calculate_pi, args=(lower, upper, i))
        t1.start()
        threads.append(t1)

    for t1 in threads:
        t1.join()

    # hitung pi
    final_result = math.sqrt(6*(sum(my_result)))
    print(final_result)
    end = time.time()
    print(end-start)
    # amati waktu eksekusi paralel, bagaimana jika banyaknya thread ditambahkan, bagaimana jika banyaknya thread dikurangi
