def freqQuery(queries):
    val_dict = {}
    freq_dict = {}
    ret_arr = []

    def change_freq(v, f, p):
        if f in freq_dict:
            freq_dict[f].add(v)
        else:
            freq_dict[f] = set()
            freq_dict[f].add(v)
        if p in freq_dict and \
        v in freq_dict[p]:
            freq_dict[p].remove(v)

    for q in queries:
        # query val
        v = None
        # next frequency
        f = None
        # previous frequency
        p = None

        # Add 1 to frequency
        if q[0] == 1:
            v = q[1]
            if v in val_dict:
                f = val_dict[v] + 1
            else:
                f = 1
            val_dict[v] = f
            p = f - 1
            change_freq(v, f, p)
            
        # subtract 1 from frequency
        elif q[0] == 2:
            v = q[1]
            if v in val_dict and val_dict[v] > 0:
                p = val_dict[v]
                f = p - 1
                change_freq(v, f, p)
                val_dict[v] = f

        elif q[0] == 3:
            v = q[1]
            if v in freq_dict and len(freq_dict[v]) > 0:
                ret_arr.append(1)
            else:
                ret_arr.append(0)

    return ret_arr