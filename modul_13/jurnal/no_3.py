# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0:
    pesan = "untuk semua rank"
    data = comm.bcast(pesan, root=0)
# jika saya bukan rank 0 maka saya menerima pesan
else:
    pesan = comm.bcast(None, root=0)
    print(f"Rank {rank} received: {pesan}")
