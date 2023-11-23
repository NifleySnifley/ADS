from generic_graph import Graph
from heapq import heappush, heappop


def dijkstra(g: Graph, start):
    prev = {start: None}
    dist = {start: 0}
    Q = [(0, start)]

    while len(Q):
        d, n = heappop(Q)

        for o in g.get_neighbors(n):
            ndist = d + g.get_weight(n, o)
            if (o not in dist) or ndist < dist[o]:
                prev[o] = n
                dist[o] = ndist
                heappush(Q, (dist[o], o))

    return dist, prev


g = Graph(False)
for e in 'uvwxyz':
    g.add_node(e)
g.connect('u', 'v', 2)
g.connect('v', 'w', 3)
g.connect('w', 'z', 5)
g.connect('z', 'y', 1)
g.connect('x', 'y', 1)
g.connect('x', 'u', 1)
g.connect('v', 'x', 2)
g.connect('u', 'w', 5)
g.connect('x', 'w', 3)
g.connect('w', 'y', 1)

# g.create_graphviz('dijkstraa')

print(dijkstra(g, 'u'))

# print(list([(n, g.get_weight('x', n)) for n in g.get_neighbors('x')]))
