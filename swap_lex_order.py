def swapLexOrder(str1, pairs):
    for p in pairs:
        p[0] -= 1
        p[1] -= 1

    a = list(str1)

    connected_dict = {}

    def add_to_dict(p0, p1):
        if p0 in connected_dict:
            connected_dict[p0].add(p[1])
        else:
            connected_dict[p0] = set([p1, p0])

    for p in pairs:
        add_to_dict(p[0], p[1])
        add_to_dict(p[1], p[0])

        for s in connected_dict[p[0]]:
            connected_dict[s] = connected_dict[s].union(connected_dict[p[1]])
        for s in connected_dict[p[1]]:
            connected_dict[s] = connected_dict[s].union(connected_dict[p[0]])


    sets = set()
    duplicates = set()
    for s in connected_dict:
        if s not in duplicates:
            sets.add(s)
            for i in connected_dict[s]:
                duplicates.add(i)
    
    arrs = []
    for s in sets:
        arrs.append(list(connected_dict[s]))

    print(sets)
    for arr in arrs:
        arr.sort(key = lambda x: a[x], reverse = True)

    print(arrs)
    retstrarr = ['']*len(str1)
    for arr in arrs:
        arr2 = sorted(arr)
        for ind, val in enumerate(arr):
            retstrarr[arr2[ind]] = str1[val]

    for i, c in enumerate(retstrarr):
        if c == '':
            retstrarr[i] = str1[i]

    return ''.join(retstrarr)

