def fibonacci(n):
    f0 = 0
    f1 = 1
    if n <= 0:
        return []
    elif n == 1:
        return [f0]
    elif n == 2:
        return [f0, f1]
    else:
        fibonacci_l = [f0, f1]

        for i in range(2, n):
            fibonacci_l.append(fibonacci_l[i - 1] + fibonacci_l[i - 2])

        return fibonacci_l
