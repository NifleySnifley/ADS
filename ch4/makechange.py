import sys, os

amount = int(sys.argv[1])
print(amount)

coins = [1, 5, 8, 10, 21, 25]


def minfn(a):
    lmin = len(a[0])
    vmin = a[0]
    for v in a:
        if (len(v) < lmin):
            lmin = len(v)
            vmin = v
    return vmin


def make_change(a):
    chgtable = {0: []}
    for am in range(1, a + 1):
        validcoins = [c for c in coins if c <= am]
        chgtable[am] = minfn([chgtable[am - c] + [c] for c in validcoins])
    return chgtable[a]


print(make_change(amount))
