def maxSubsetSum(arr):
    cache = {}
    temp = []
    # Isolates islands of positive numbers
    for i in arr:
        if i > 0:
            temp.append(i)
        else:
            if len(temp) > 0:
                if len(temp) in cache:
                    cache[len(temp)].append(temp)
                else:
                    cache[len(temp)] = [temp]
                temp = []
    if len(temp) > 0:
        if len(temp) in cache:
            cache[len(temp)].append(temp)
        else:
            cache[len(temp)] = [temp]

    
    # Recursive method to find sub sum
    def find_sub_sum(sub_arr):
        if len(sub_arr) == 1:
            return sub_arr[0]
        elif len(sub_arr) == 2:
            return max(sub_arr)
        else:
            max_sum = 0
            for ind, i in enumerate(sub_arr):
                if ind < 2:
                    max_sum = max(max_sum, i + find_sub_sum(sub_arr[ind+2:]))
                elif ind > len(sub_arr) - 2:
                    max_sum = max(max_sum, i + find_sub_sum(sub_arr[0:ind-1]))
                else:
                    max_sum = max(max_sum, i + find_sub_sum(sub_arr[0:ind-1]) +\
                                find_sub_sum(sub_arr[ind+2:]))
            return max_sum

    sum = 0
    for i in cache:
        for j in cache[i]:
            sum += find_sub_sum(j)
            
    return sum