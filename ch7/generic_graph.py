from collections import defaultdict
import tempfile
import graphviz


class Graph():
    def __init__(self, directed=True):
        self.nodes = set()
        self.edges = defaultdict(lambda: {})
        self.dir = directed

    def add_node(self, n):
        self.nodes.add(n)

    def connect(self, a, b, weight=None):
        # if (a not in self.nodes) or (b not in self.nodes):
        #     return
        self.edges[a][b] = weight
        if not self.dir:
            self.edges[b][a] = weight

    def get_neighbors(self, n):
        return [v for v, w in self.edges[n]]

    def get_weight(self, fro, to):
        return self.edges[fro][to] if (fro in self.edges and to in self.edges[fro]) else None

    def create_graphviz(self, outname):
        g = graphviz.Digraph(outname, engine='neato')
        for n in self.nodes:
            g.node(str(n))
        for src, dsts in self.edges.items():
            for dst, w in dsts.items():
                g.edge(str(src), str(dst), label=str(
                    w) if w is not None else None)

        g.render(tempfile.mktemp('.gv'), format="svg", view=True)
        # g.render("out.gv", format="png")

    def __contains__(self, n):
        return n in self.nodes

    def __iter__(self):
        return self.nodes.__iter__()


if __name__ == "__main__":
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node("yay")
    g.connect(1, 2)
    g.connect(2, 3)
    g.connect(3, 1)
    g.connect(3, 'yay', 1234)

    g.create_graphviz("Grapheee!")
