import functools


@functools.cache
def collen(n: int):
    if (n == 1):
        return 1
    elif (n & 1):
        return 1 + collen(3 * n + 1)
    else:
        return 1 + collen(n // 2)


print(max(range(1, 1000000), key=collen))
