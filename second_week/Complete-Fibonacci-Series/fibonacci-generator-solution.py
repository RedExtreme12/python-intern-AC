def fibonacci(n):
    return [elem for elem in fibonacci_seq_generator(n)]


def fibonacci_seq_generator(n):
    f0 = 0
    f1 = 1
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0 + f1
