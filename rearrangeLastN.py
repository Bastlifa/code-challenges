def rearrangeLastN(l, n):

    if l is None:
        return l
    p1 = l
    p2 = l
    count = 0
    while p1.next is not None:
        p1 = p1.next
        count += 1
        if count > n:
            p2 = p2.next

    ret_head = l
    if count > n - 1:
        p1.next = l
        ret_head = p2.next
        p2.next = None

    return ret_head