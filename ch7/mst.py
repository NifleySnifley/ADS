from generic_graph import Graph
from heapq import heappush, heappop, heapify
import graphviz, tempfile

g = Graph(False)
for n in range(ord('A'), ord('G') + 1):
    g.add_node(chr(n))

# Book
g.connect('A', 'B', 2)
g.connect('A', 'C', 3)
g.connect('B', 'C', 1)
g.connect('B', 'D', 1)
g.connect('B', 'E', 4)
g.connect('C', 'F', 5)
g.connect('D', 'E', 1)
g.connect('E', 'F', 1)
g.connect('F', 'G', 1)

# Wikipedia Kruskal's
# g.connect('A', 'B', 7)
# g.connect('B', 'C', 8)
# g.connect('A', 'D', 5)
# g.connect('B', 'D', 9)
# g.connect('B', 'E', 7)
# g.connect('C', 'E', 5)
# g.connect('D', 'E', 15)
# g.connect('D', 'F', 6)
# g.connect('E', 'F', 8)
# g.connect('F', 'G', 11)
# g.connect('E', 'G', 9)


# Apparently this is Kruskal's algorithm
def get_mst_kruskal(g: Graph):
    es = list(g.get_edges())
    heapify(es)

    mst = []

    # Stupid disjoint set that never deleted unioned sets
    # Just unions to the smaller index so the first (unioned) set
    # is the first index to be found for a given item
    dsets = [set({n}) for n in g.nodes]

    def find_s(t):
        return [i for i, e in enumerate(dsets) if t in e][0]

    def union_s(i1: int, i2: int):
        dsets[min(i1, i2)].update(dsets[max(i1, i2)])

    while len(es):
        w, a, b = heappop(es)
        ai = find_s(a)
        bi = find_s(b)
        if ai != bi:
            mst.append(tuple(sorted((a, b))))
            union_s(ai, bi)

    return mst


def get_mst_prim(g: Graph):
    start = next(g.nodes.__iter__())

    dist = {n: 10000000 for n in g.nodes}
    dist[start] = 0

    q = [(v, k) for k, v in dist.items()]
    heapify(q)

    prev = {n: None for n in g.nodes}

    while len([v for k, v in dist.items() if v < 10000000]) != len(g.nodes):
        d, n = heappop(q)
        for nb in g.get_neighbors(n):
            td = g.get_weight(n, nb)
            if td < dist[nb]:
                dist[nb] = td
                prev[nb] = n
                heappush(q, (td, nb))
        pass

    mst = []

    for to, fro in prev.items():
        if to is not None and fro is not None:
            mst.append(tuple(sorted((to, fro))))

    return mst


if __name__ == "__main__":
    print(get_mst_prim(g))

    print(get_mst_kruskal(g))

    mst = get_mst_kruskal(g)
    g.create_graphviz(
        "mst",
        eparams=lambda (a, b, w):
        {"color": "green" if (a, b) in mst or (b, a) in mst else "black"})
    # gv = graphviz.Graph(engine='neato')

    # for n in g.nodes:
    #     gv.node(str(n))
    # for src, dsts in g.edges.items():
    #     for dst, w in dsts.items():
    #         ismst = (src, dst) in mst or (dst, src) in mst
    #         gv.edge(str(src),
    #                 str(dst),
    #                 label=str(w) if w is not None else None,
    #                 color="green" if ismst else 'black',
    #                 penwidth="2" if ismst else "1")

    # gv.render(tempfile.mktemp('.gv'), format="svg", view=True)
