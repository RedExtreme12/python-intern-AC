def tribonacci(signature, n):
    return [elem for elem in tribonacci_seq_generator(signature, n)]


def tribonacci_seq_generator(signature, n):
    f0, f1, f2 = signature
    for _ in range(n):
        yield f0
        f0, f1, f2 = f1, f2, f1 + f2 + f0
