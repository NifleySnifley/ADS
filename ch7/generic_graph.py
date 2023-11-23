from collections import defaultdict
import tempfile
import graphviz


class Graph:

    def __init__(self, directed=True):
        self.nodes = set()
        self.edges = defaultdict(dict)
        self.erevs = defaultdict(dict)
        self.dir = directed

    def add_node(self, n):
        self.nodes.add(n)

    def get_edges(self):
        return {(w, a, b) for a, u in self.edges.items() for b, w in u.items()}

    def connect(self, a, b, weight=None):
        self.edges[a][b] = weight
        self.erevs[b][a] = weight

    def get_neighbors(self, n):
        if self.dir:
            return [v for v, w in self.edges[n].items()]
        else:
            return [v for v, w in self.edges[n].items()
                    ] + [v for v, w in self.erevs[n].items()]

    def get_weight(self, fro, to):
        if self.dir:
            return self.edges[fro][to] if (fro in self.edges
                                           and to in self.edges[fro]) else None
        else:
            e1 = self.edges[fro][to] if (fro in self.edges
                                         and to in self.edges[fro]) else None
            e2 = self.erevs[fro][to] if (fro in self.erevs
                                         and to in self.erevs[fro]) else None
            return e2 if e1 is None else e1

    def create_graphviz(self,
                        outname,
                        engine="neato",
                        fname=None,
                        fmt=None,
                        view=True,
                        gparams={},
                        nparams=lambda n: {},
                        eparams=lambda e: {}):
        g: graphviz.Graph | graphviz.Digraph | None = None
        if self.dir:
            g = graphviz.Digraph(outname, engine=engine, graph_attr=gparams)
        else:
            g = graphviz.Graph(outname, engine=engine, graph_attr=gparams)
            pass

        for n in self.nodes:
            g.node(str(n), **nparams(n))
        for src, dsts in self.edges.items():
            for dst, w in dsts.items():
                g.edge(str(src),
                       str(dst),
                       label=str(w) if w is not None else None,
                       **eparams((src, dst, w)))

        g.render(fname if fname is not None else tempfile.mktemp('.gv'),
                 format="svg" if fmt is None else fmt,
                 view=view)

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
