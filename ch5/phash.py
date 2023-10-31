import numpy as np


def phash(items):
    # My own stupid implementation: hash each item, and create a polynomial that assigns each hash to len(items) consecutive integers
    # TODO: Find a proper way to remove collisions
    xs = [hash(i) % len(items * 4) for i in items]
    N = len(items)
    # find P(h) so that P(hash(i)) = items.index(i)
    print([f"{xs[i]} -> {i}" for i in range(N)])

    X = np.array([[xs[i]**n for n in range(N)] for i in range(N)])
    print(X)
    Y = np.array([[i] for i in range(N)])
    print(Y)
    B = np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)),
                  np.matmul(np.transpose(X), Y))
    print(B)

    def hashfn(item):
        h = hash(item) % (N * 4)
        return int(sum([(h**n) * B[n] for n in range(N)]))

    return hashfn


items = [
    "one",
    "two",
    "three",
    # "four",
    # "five",
    # "six",
    # "seven",
]

hf = phash(items)
print(hf("one"))
print(hf("two"))
print(hf("three"))

# Disclaimer: this is a terrible idea and it only works occasionally...
# TODO: Actually make a perfect hash!
