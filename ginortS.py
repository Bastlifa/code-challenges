import functools
s = input()
nums = [str(i) for i in range(1,10)]

def sorter(a,b):
    if a in nums and b in nums:
        i_a = int(a)
        i_b = int(b)
        if i_a%2 == 0 and i_b%2 == 0:
            if i_a < i_b:
                return -1
            elif i_a > i_b:
                return 1
            else:
                return 0
        elif i_a%2 == 1 and i_b%2 == 0:
            return -1
        elif i_a%2 == 0 and i_b%2 == 1:
            return 1
        else:
            if i_a < i_b:
                return -1
            elif i_a > i_b:
                return 1
            else:
                return 0
    elif a in nums and b not in nums:
        return 1
    elif a not in nums and b in nums:
        return -1
    else:
        if a == a.upper() and b == b.upper():
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0
        elif a != a.upper() and b != b.upper():
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0
        elif a != a.upper() and b == b.upper():
            return -1
        elif a == a.upper() and b != b.upper():
            return 1

s_arr = [c for c in s]


print(''.join(sorted(s_arr, key=functools.cmp_to_key(sorter))))