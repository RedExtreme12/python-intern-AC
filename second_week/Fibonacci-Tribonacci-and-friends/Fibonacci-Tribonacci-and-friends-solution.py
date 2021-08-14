from copy import copy


def Xbonacci(signature, n):
    return [elem for elem in Xbonacci_seq_generator(signature, n)]


def Xbonacci_seq_generator(signature, n):
    seq = copy(signature)

    for sig_elem in seq:
        yield sig_elem

    for _ in range(n - len(seq)):
        next_elem = sum(seq)
        seq = seq[1:] + [next_elem]

        yield next_elem
