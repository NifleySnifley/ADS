items = [  # Weight, value
    (2, 3), (3, 4), (4, 8), (5, 8), (9, 10)
]


def maxknapsackv(weight):
    if (weight < min([i[0] for i in items])):
        return 0
    else:
        fit = [i for i in items if i[0] <= weight]
        return max([maxknapsackv(weight - f[0]) + f[1] for f in fit])


print(maxknapsackv(20))
