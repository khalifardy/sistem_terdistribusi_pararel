# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank terbesar maka say\
#  akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == size-1:
    for i in range(size-1):
        pesan = f"haloo rank - {i}"
        comm.send(pesan, i)
else:
    pesan_max = comm.recv(source=size - 1)
    print(f"Proses dengan rank {rank} menerima pesan: {pesan_max}")
