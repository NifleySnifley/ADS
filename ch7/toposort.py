input = [
    tuple(i.split(' -> ')) for i in """Milk -> Mix
Egg -> Mix
Oil -> Mix
Griddle -> Pour
Mix -> Pour
Pour -> Flip
Flip -> Eat
Syrup -> Eat
Mix -> Syrup""".splitlines()
]

workitems = set([i[0] for i in input] + [i[1] for i in input])

prereqs = {k: [reqmt for reqmt, I in input if k == I] for k in workitems}
# print(prereqs)

seq = []
while len(workitems):
    valids = sorted([
        i for i in workitems
        if len(prereqs[i]) == 0 or all(v in seq for v in prereqs[i])
    ])
    if not len(valids):
        print("Error, not able to complete tasks")
    ni = valids[0]
    workitems.remove(ni)
    seq.append(ni)

print(seq)
