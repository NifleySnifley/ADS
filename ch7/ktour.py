from collections import deque, defaultdict
from matplotlib import pyplot as plt
import math
import sys

BOARDSIZE = 40
sys.setrecursionlimit(sys.getrecursionlimit()*4)


def c_to_b(c: complex):
    return 1 << (int(c.real) * BOARDSIZE + int(c.imag))


def b_to_c(c: int):
    c = math.log2(c)
    return (c // BOARDSIZE) + 1j * (c % BOARDSIZE)


def kmoves(c: complex):
    for o in [2-1j, 2+1j, 1+2j, 1-2j, -2-1j, -2+1j, -1+2j, -1-2j]:
        adj = o + c
        if 0 <= int(adj.real) < BOARDSIZE and 0 <= int(adj.imag) < BOARDSIZE:
            yield adj


nbrs = {}
for x in range(BOARDSIZE):
    for y in range(BOARDSIZE):
        Z = x+1j*y
        nbrs[c_to_b(Z)] = [c_to_b(m) for m in kmoves(Z)]

tourdone = (2**(BOARDSIZE**2)) - 1
start = 0+0j

prev = {c_to_b(start): None}
fnode = None

visited = c_to_b(start)


def gettour(node):
    global prev, fnode, visited

    visited |= node
    # print(bin(visited))
    if (visited.bit_count() == (BOARDSIZE**2)):
        fnode = node
        print("Finished!")
        return True
    else:
        nbrs[node].sort(key=lambda c: len(
            [n for n in nbrs[c] if not (visited & n)]))
        for p in nbrs[node]:
            if not (visited & p):
                prev[p] = node
                if (gettour(p)):
                    return True

        visited &= ~node
    return False


gettour(c_to_b(start))

pth = [fnode]
while prev[pth[-1]] is not None:
    pth.append(prev[pth[-1]])
pth.reverse()

pth = [b_to_c(p) for p in pth]
print(' -> '.join([f"({c.real:.0f}, {c.imag:.0f})" for c in pth]))

plt.axes().set_aspect(1.0)
plt.plot([n.real for n in pth], [n.imag for n in pth])
plt.scatter([n.real for n in pth], [n.imag for n in pth], c='green')
plt.show()
