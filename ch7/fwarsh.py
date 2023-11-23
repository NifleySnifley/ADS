from generic_graph import Graph
from collections import defaultdict, deque
import sys

g = Graph()

for n in '1234':
    g.add_node(n)
g.connect('1', '3', -2)
g.connect('3', '4', 2)
g.connect('4', '2', -1)
g.connect('2', '1', 4)
g.connect('2', '3', 3)


# One nice thing about this it seems is that it only needs two fixed-size matrices
# Might work well for SciOly, since it's only a 4x4 grid so there would be 64 loop cycles (O(N^3))
def fwarsh(g: Graph):
    # Wow autopep8 butchered this
    dist = defaultdict(lambda: defaultdict(lambda: sys.maxsize))
    prev = defaultdict(lambda: defaultdict(lambda: None))

    for n in g.nodes:
        dist[n][n] = 0
        prev[n][n] = n
    for w, u, v in g.get_edges():
        dist[u][v] = w
        prev[u][v] = u

    for k in g.nodes:
        for i in g.nodes:
            for j in g.nodes:
                # If the distance from I to J is greater than the distance from I to J via K,
                # Then travelling via K is shorter!
                ij_via_k = dist[i][k] + dist[k][j]
                if dist[i][j] > ij_via_k:
                    dist[i][j] = ij_via_k
                    # When going from I to J you would first need to go to K!
                    prev[i][j] = prev[k][j]
    return dist, prev


def getpath(prevs, u, v):
    p = [v]
    while u != v:
        v = prevs[u][v]
        p.append(v)
    p.reverse()
    return p


d, prevs = fwarsh(g)
nsort = list(g.nodes)
nsort.sort()

BOLD = "\033[1m"
RST = "\033[0m"

print(BOLD + ' ' * 4 + ' '.join([str(n).ljust(3) for n in nsort]) + "\n" + RST)
for a in nsort:
    print(BOLD + str(a).ljust(4), end=RST)
    for b in nsort:
        print(str(d[a][b]).ljust(3), end=' ')
    print('\n')

print()
print(getpath(prevs, '3', '1'))
