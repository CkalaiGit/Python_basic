rank1 = 1
def recusif_fibonacci(rank):
    if rank == 1 or rank == 0: return rank1
    return recusif_fibonacci(rank - 1) + recusif_fibonacci(rank - 2)


def iteratif_fibonacci(rank):
    if rank == 1 or rank == 0:  return rank1

    fibNMinus1 = 1
    fibNMinus2 = 1
    fibN = 0
    for i in range(2, rank + 1):
        fibN = fibNMinus1 + fibNMinus2
        fibNMinus2 = fibNMinus1
        fibNMinus1 = fibN
    
    return fibN


