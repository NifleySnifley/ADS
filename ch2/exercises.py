from random import randint

# O(n log n + n + 1) or simply O(n log n)


def kmin(values, k):
    values.sort()  # O(n log n)
    ret = []
    # O(n)
    for i in range(len(values)):
        if not ret or ret[-1] != values[i]:
            ret.append(values[i])

    return ret[k]  # O(1)


# Worst case O(n+k) where k is the range of the array
def kmin_linearish(values, K):
    mi = min(values)
    span = max(values) - mi  # O(n)
    counts = [0] * (span + 1)

    # O(n)
    for item in values:
        counts[item-mi] = 1

    # O(k) worst case
    c = 0
    for i, v in enumerate(counts):
        if (v == 1):
            if (c == K):
                return i+mi
            c += 1

    return len(counts)


vals = [randint(-100, 100) for i in range(20)]
# print(list(sorted(list(set(vals)))))

for i in range(len(set(vals))):
    print(
        f"kmin({i}) = {kmin(vals.copy(), i)} = {kmin_linearish(vals.copy(), i)}"
    )
