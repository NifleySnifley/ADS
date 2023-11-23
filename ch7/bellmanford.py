from generic_graph import Graph
import sys
from collections import deque

g = Graph()
for l in 'stxyz':
    g.add_node(l)

g.connect('s', 't', 6)
g.connect('t', 'x', 5)
g.connect('t', 'y', 8)
g.connect('s', 'y', 7)
g.connect('y', 'z', 9)
g.connect('t', 'z', -4)
g.connect('y', 'x', -3)
g.connect('z', 'x', 7)
g.connect('x', 't', -2)


def bellford(g: Graph, start):
    dist = {n: sys.maxsize for n in g.nodes}
    prev = {n: None for n in g.nodes}
    dist[start] = 0

    # Ahh this makes sense!
    for i in range(len(g.nodes)):
        for w, u, v in g.get_edges():
            ndist = dist[u] + w
            if ndist < dist[v]:
                dist[v] = ndist
                prev[v] = u
    print(dist)

    # Don't worry about this if there aren't any cycles
    # But I have a feeling that this might come in handy in a future/past AOC solution hehe!
    for w, u, v in g.get_edges():
        if dist[u] + w < dist[v]:
            prev[v] = u
            vis = {v}
            while u not in vis:
                vis.add(u)
                u = prev[u]
            # TODO: Check the correctness of this
            ncycle = deque([u])
            v = prev[u]
            while v != u:
                ncycle.appendleft(v)
                v = prev[v]
            print(f"Cycle!: {ncycle}")

    return dist, prev


dists = bellford(g, 's')
print(dists)
