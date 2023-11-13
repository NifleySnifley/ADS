from collections import deque
from generic_graph import Graph
dictionary = {word.strip() for word in open("./words_alpha.txt").readlines()}


def transform_seq(start, end):
    print(len(start), len(end))
    prev = {start: None}
    Q = deque([start])
    while len(Q):
        ow = Q.popleft()

        # print(ow)
        if ow == end:
            print("done")
            break

        else:
            for i in range(len(start)):
                for l in range(ord('a'), ord('z')+1):
                    w = ow[:i] + chr(l) + ow[i+1:]
                    if w in dictionary and w not in prev:
                        Q.append(w)
                        prev[w] = ow

    # Don't do this to your computer...

    # g = Graph()
    # for k, v in prev.items():
    #     if (k is None) or (v is None):
    #         continue
    #     g.add_node(k)
    #     g.connect(v, k)
    # print(g.edges)
    # g.create_graphviz("Woah")

    # print(prev)
    pth = [end]
    while pth[-1] != None:
        if pth[-1] not in prev:
            return ["Unreachable"]
        pth.append(prev[pth[-1]])
    pth.pop()
    pth.reverse()
    return pth


print(" -> ".join(transform_seq("tipsy", "eagle")))
