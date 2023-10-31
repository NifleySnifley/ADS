import random, timeit


# Bubblesort, in place
def bbsort(arr):
    chg = True
    while (chg):
        chg = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                chg = True

    return


# Selection sort, in place
def ssort(arr):
    for i in range(1, len(arr)):
        maxidx = max(enumerate(arr[:len(arr) - i + 1]), key=lambda t: t[1])[0]
        arr[len(arr) - i], arr[maxidx] = arr[maxidx], arr[len(arr) - i]


# Insertion sort, in place
def isort(arr):
    for i in range(1, len(arr)):
        for j in range(0, i):
            if (arr[i - j] <= arr[i - j - 1]):
                arr[i - j], arr[i - j - 1] = arr[i - j - 1], arr[i - j]


# In-place insertion sort with stride for shellsort
def isort_stride(arr, start, stride):
    for i in range(start, len(arr), stride):
        for j in range(0, i, stride):
            if (arr[i - j] <= arr[i - j - stride]):
                arr[i - j], arr[i - j - stride] = arr[i - j - stride], arr[i -
                                                                           j]


# Shell sort, in place
def shellsort(arr):
    nsubs = len(arr) // 2
    while nsubs > 0:
        for start in range(nsubs):
            isort_stride(arr, start, nsubs)
        nsubs //= 2


# TODO: More efficient merge!
def merge(a, b):
    ai, bi = 0, 0
    out = []
    while (ai < len(a) or bi < len(b)):
        if (ai < len(a)) and ((bi == len(b)) or (a[ai] <= b[bi])):
            out.append(a[ai])
            ai += 1
        else:
            out.append(b[bi])
            bi += 1
    return out


# Merge sort, not in place
# TODO: Implement an in-place merge
def mergesort(arr):
    pivot = (len(arr) - 1) // 2
    if (len(arr) <= 2):
        return [min(arr), max(arr)] if len(arr) == 2 else arr
    else:
        return merge(mergesort(arr[:pivot]), mergesort(arr[pivot:]))


def ms_inplace_wrapper(l):
    std = mergesort(l)
    for i in range(len(std)):
        l[i] = std[i]


def qsort(arr):
    quicksort(arr, 0, len(arr) - 1)


def quicksort(arr, a, b):
    if (a >= b):
        return
    i = partition(arr, a, b)
    quicksort(arr, a, i - 1)
    quicksort(arr, i + 1, b)


# I implemented the standard "original" partition method (From my CLRS textbook)
# as opposed to the Hoare partition from the textbook
def partition(arr, a, b):
    # For the original sort, pvi := r, for randomized qsort, this works
    #pvi = random.randint(a, b)
    # This implements the "median of three" partitioning method
    pvi = sorted([random.randint(a, b) for i in range(3)],
                 key=lambda i: arr[i])[1]

    arr[pvi], arr[b] = arr[b], arr[pvi]

    pivot = arr[b]
    i = a - 1
    for j in range(a, b):
        if (arr[j] <= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1

    arr[i], arr[b] = arr[b], arr[i]
    return i


list = [26, 54, 93, 17, 77, 31, 44, 55, 20]

sorts = [
    bbsort, ssort, isort, shellsort, ms_inplace_wrapper, qsort,
    lambda e: e.sort()
]
trials = 5
slists = [[random.randint(0, 2048) for i in range(500)] for i in range(trials)]


def sproffn(sfn):
    tlists = [i.copy() for i in slists]

    def proffn():
        slist = tlists.pop()
        sfn(slist)

    return proffn


# for s in sorts:
#     res = timeit.timeit(sproffn(s), number=trials) / trials
#     print(res)

# bblist = list.copy()
# bbsort(bblist)
# print(bblist)

# sslist = list.copy()
# ssort(sslist)
# print(sslist)

# islist = list.copy()
# isort(islist)
# print(islist)

# sstlist = list.copy()
# shellsort(sstlist)
# print(sstlist)

# mslist = list.copy()
# mslist = mergesort(mslist)
# print(mslist)

qsort(list)
print(list)
