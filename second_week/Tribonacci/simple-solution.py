def tribonacci(signature, n):
    f0, f1, f2 = signature
    if n == 0:
        return []
    if n == 1:
        return [f1]
    elif n == 2:
        return [f2]
    else:
        tribonacci = [f0, f1, f2]

        for i in range(3, n):
            tribonacci.append(tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3])

        return tribonacci
