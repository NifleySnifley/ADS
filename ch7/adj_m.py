from generic_graph import Graph

keys = "ABCDEF"
am = ["075001", "200730", "020008", "100024", "600500", "010080"]

g = Graph()
for k in keys:
    g.add_node(k)

for r in range(len(am)):
    for c in range(len(am[0])):
        cn = int(am[r][c])
        if cn:
            g.connect(keys[r], keys[c], cn)

g.create_graphviz("Exercise 1",
                  engine='dot',
                  fname='e1',
                  fmt='png',
                  view=False)

g2 = Graph()
il = [
    1, 2, 10, 1, 3, 15, 1, 6, 5, 2, 3, 7, 3, 4, 7, 3, 6, 10, 4, 5, 7, 6, 4, 5,
    5, 6, 13
]

for i in range(len(il) // 3):
    t, f, w, *_ = il[i * 3:]
    print(t, f, w)
    g2.add_node(t)
    g2.add_node(f)
    g2.connect(t, f, w)

g2.create_graphviz("Exercise 2",
                   fname='e2',
                   fmt='png',
                   eparams=lambda *a: {'len': '2.0'})
