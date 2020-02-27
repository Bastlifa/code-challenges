def minimumBribes(q):

    min_bribes = 0
    clean_pass = False
    while clean_pass == False:
        clean_pass = True
        for i, val in enumerate(q):
            if i < len(q) - 1 and val > q[i + 1]:
                if val - (i+1) > 2:
                    print("Too chaotic")
                    return
                clean_pass = False
                temp = val
                q[i] = q[i+1]
                q[i+1] = temp
                min_bribes += 1
    print(min_bribes)