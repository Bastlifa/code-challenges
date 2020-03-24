def possibleSums(coins, quantity):

    sums_cache = set()

    coins_dict = {}

    for i, c in enumerate(coins):
        if c not in coins_dict:
            coins_dict[c] = quantity[i]
        else:
            coins_dict[c] += quantity[i]

    def find_sums(c, count):
        temp_sums = set()
        for i in range(1, count + 1):
            for s in sums_cache:
                temp_sums.add(c * i + s)
            temp_sums.add(c * i)
        for ts in temp_sums:
            sums_cache.add(ts)
    
    for c in coins_dict:
        find_sums(c, coins_dict[c])

    return len(sums_cache)

