def avoidObstacles(inputArray):

    a = max(inputArray)
    for i in range(1, a + 2):
        conflict = False
        for inp in inputArray:
            if inp % i == 0:
                conflict = True
                break
        if not conflict:
            return i
