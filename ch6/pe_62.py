import math, itertools
from collections import defaultdict

cubes = {i**3 for i in range(10000)}

maxes = {i: int(''.join(sorted(list(str(i))))) for i in cubes}


def iscube(n):
    return n in cubes
    # return round((math.pow(n, 1 / 3) % 1), 9) in [1.0, 0.0]


# print(maxes)

ms = defaultdict(lambda: [])
for k, v in maxes.items():
    ms[v].append(k)

m5s = [k for k in ms.keys() if len(ms[k]) == 5]
print(m5s)

print(
    min([
        min([
            int(''.join(perm)) for perm in itertools.permutations(list(str(n)))
            if iscube(int(''.join(perm)))
        ]) for n in m5s
    ]))

# print(iscube(1234**3))
# print(iscube((345**3) - 1))

# #1032
# for n in range(0, 2000):
#     cube = n * n * n
#     digits = list(str(cube))
#     lcb = len([
#         1 for n in {int(''.join(e))
#                     for e in itertools.permutations(digits)} if iscube(n)
#     ])
#     print(n, lcb)
#     if lcb == 5:
#         break
