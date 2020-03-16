def isCryptSolution(crypt, solution):
    words = {i: "" for i in range(3)}

    sol_dict = {i[0]: i[1] for i in solution}

    for i in range(len(crypt)):
        for j in range(len(crypt[i])):
            words[i] += sol_dict[crypt[i][j]]

    for i in words:
        if words[i][0] == '0' and len(words[i]) > 1:
            return False

    if int(words[0]) + int(words[1]) == int(words[2]):
        return True
    
    return False