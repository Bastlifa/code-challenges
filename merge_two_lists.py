def findMergeNode(head1, head2):

    pointer_set = set()
    pointer_set.add(head1)
    pointer_set.add(head2)

    cur1 = head1
    cur2 = head2

    while cur1 is not None or cur2 is not None:
        # print(pointer_set)
        if cur1 is not None:
            cur1 = cur1.next
            if cur1 is not None:
                if cur1 in pointer_set:
                    return cur1.data
                else:
                    pointer_set.add(cur1)
        if cur2 is not None:
            cur2 = cur2.next
            if cur2 is not None:
                if cur2 in pointer_set:
                    return cur2.data
                else:
                    pointer_set.add(cur2)