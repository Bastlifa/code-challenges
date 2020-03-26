def isIPv4Address(inputString):
    arr = inputString.split('.')

    if len(arr) != 4:
        return False

    digs = [str(i) for i in range(10)]

    for num in arr:
        if len(num) == 0 or len(num) > 3:
            return False
        for c in num:
            if c not in digs:
                return False
        if int(num) > 255 or int(num) < 0 or (len(num) > 1 and num[0] == '0'):
            return False
    
    return True