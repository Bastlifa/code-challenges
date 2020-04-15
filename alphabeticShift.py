def alphabeticShift(inputString):
    split_string = list(inputString)
    for i, c in enumerate(split_string):
        if c == 'z':
            split_string[i] = 'a'
        else:
            split_string[i] = chr(ord(c) + 1)
    return ''.join(split_string)

