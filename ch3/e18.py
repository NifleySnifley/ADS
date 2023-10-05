numers = [1, 5, 12, 2, 4, 6, 23, 1, 5, 17, 4, 4, 7, 9, 2, 3]
print(list(sorted(numers)))


def radixsort(numers):
    core = numers.copy()
    bins = [[] for i in range(10)]
    digit = 0
    while 1:
        digit += 1
        while len(core):
            numer = core.pop()
            bins[(numer % (10**digit)) // (10**(digit - 1))].append(numer)

        l0 = len(bins[0])

        for i in range(len(bins)):
            while (len(bins[i])):
                core.append(bins[i].pop())

        if (l0 == len(numers)):
            break

    return core


print(radixsort(numers))
