graph = {
    "A": "B",
    "B": "CE",
    "C": "CF",
    "D": "BG",
    "E": "DA",
    "F": "H",
    "G": "E",
    "H": "I",
    "I": "F",
}
nodes = set(graph.keys())


# I have no idea what the actual algorithm is to do this, start stop times, etc.
# I just did it the way I found intuitive
def find_sccs(node, pth=[], ccs=[], bs=True):
    for n in graph[node]:
        # If there is a cycle, take the nodes in the cycle and save them for later
        if n in pth:
            clique = pth[pth.index(n):]
            ccs.append(clique)
        else:
            pth.append(n)
            find_sccs(n, pth, ccs, False)
            pth.pop()
    pass

    # Base Case
    if bs:
        cl = []
        # Each SCC can contain multiple groups, so merge them
        # Could be optimized with hashmap instead of search, but this is fine for now
        for c in map(set, ccs):
            cps = ([i for i, b in enumerate(cl) if len(c.intersection(b))] +
                   [-1])[0]
            if cps != -1:
                cl[cps].update(c)
            else:
                cl.append(c)
        return cl


print(find_sccs('A'))
