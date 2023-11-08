import math
import itertools

lns = [
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,1),(2,2),(3,3)],
    [(3,0),(2,1),(1,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],    
]

gd = [list(map(int, ln.strip().split())) for ln in open("./pe_11.txt").readlines()]

print(max([max([math.prod([gd[x][y]for x,y in[tuple(map(sum,zip(c,o)))for c in l]]) for l in lns if all([all([0<=c<20 for c in p])for p in[tuple(map(sum,zip(c,o))) for c in l]])]+[0]) for o in itertools.product(range(20),range(20))]))

# pd= 0
# for x in range(20):
#     for y in range(20):
#         o = (x,y)
#         for l in lns:
#             lcs = list([tuple(map(sum, zip(c,o))) for c in l])
#             if all([all([0 <= c < 20 for c in p]) for p in lcs]):
#                 pd = max(pd, math.prod([
#                     gd[x][y] for x,y in lcs
#                 ]))

# print(pd)