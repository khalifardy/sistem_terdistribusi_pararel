from mpi4py import MPI
import random

# Inisialisasi COMM
comm = MPI.COMM_WORLD

# Dapatkan rank proses
rank = comm.Get_rank()

# Dapatkan total proses berjalan
size = comm.Get_size()

# Generate angka integer secara random untuk setiap proses
random_number = random.randint(1, 100)

# Jika saya adalah proses dengan rank 0
if rank == 0:
    total_sum = random_number  # Inisialisasi nilai total_sum dengan nilai proses 0

    # Menerima nilai dari proses 1 s.d proses dengan rank terbesar
    for i in range(1, size):
        received_number = comm.recv(source=i)
        total_sum += received_number

    print(f"Proses {rank} - Total Sum: {total_sum}")

# Jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    comm.send(random_number, dest=0)
