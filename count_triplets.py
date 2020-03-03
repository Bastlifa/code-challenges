import math
def countTriplets(arr, r):

    if r == 1:
        vals = {}
        for a in arr:
            if a in vals:
                vals[a] += 1
            else:
                vals[a] = 1
        t = 0
        for a in vals:
            n = vals[a] - 2
            for i in range(n):
                t += (n-i)*(n - i + 1)/2
        return math.floor(t)

    triplets = 0

    val_dict = {}

    def add_or_increase(d, k, i, ind):
        if k in d:
            d[k][ind] += i
        else:
            d[k] = [0,0]
            d[k][ind] = i
        return

    for i, a in enumerate(arr):
        if a/r in val_dict:
            add_or_increase(val_dict, a, val_dict[a/r][0], 1)
            add_or_increase(val_dict, a, 1, 0)
            if i > 1:
                triplets += val_dict[a/r][1]
        else:
            add_or_increase(val_dict, a, 1, 0)

    return triplets