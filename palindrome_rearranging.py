def palindromeRearranging(inputString):
    odds = 0
    char_dict = {}
    for c in inputString:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    for c in char_dict:
        if char_dict[c] % 2 == 1:
            odds += 1

    if odds > 1:
        return False
    else:
        return True