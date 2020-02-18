def equalizeArray(arr):
    if len(arr) == 0: return 0
    numDict = {}
    for a in arr:
        if a in numDict:
            numDict[a] += 1
        else: numDict[a] = 1
    
    most = arr[0]
    for n in numDict:
        if numDict[n] > numDict[most]:
            most = n
    
    removals = 0

    for a in arr:
        if a != most:
            removals += 1

    return removals