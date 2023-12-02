# buatlah fungsi untuk menghitung pi menggunakan Riemann zeta function
# (pi^2)/6 = 1/(1^2)+ 1/(2^2) + 1/(3^2) + 1/(4^2) + ...
import time
import math


def calculate_pi(lower, upper):
    result = 0
    for i in range(lower, upper):
        result += 1/(i**2)

    result = math.sqrt(6*result)

    return result


start = time.time()
# panggil fungsi calculate_pi indek 1 sampai 10000
result = (calculate_pi(1, 10000))
print(result)
end = time.time()
print(end-start)

# amati waktu eksekusi seria
