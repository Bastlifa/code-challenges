def arrangeCoins(self, n: int) -> int:
    i = 0
    while n >= i*(i+1)/2:
        i = i + 1
    i = i - 1
    
    return i