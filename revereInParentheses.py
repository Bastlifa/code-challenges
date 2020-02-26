def areSimilar(a, b):
    unequal_a = []
    unequal_b = []

    for i, val in enumerate(a):
        if val != b[i]:
            unequal_a.append(val)
            unequal_b.append(b[i])

    if len(unequal_a) <= 2:
        for val in unequal_a:
            if val not in unequal_b:
                return False
        return True
    return False