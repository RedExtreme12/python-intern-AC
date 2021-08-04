def prefill(n,v):
    if not isinstance(n, int):
        raise TypeError(f'{n} is invalid')
    else:
        return [v for _ in range(n)]
