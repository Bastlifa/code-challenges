function removeNodes(listHead, x) {
    // Write your code here
    while(listHead && listHead.data > x)
    {
        listHead = listHead.next
    }
    let cur = listHead
    let prev = null
    while(cur && cur.next)
    {
        if(cur.next.data <= x)
        {
            prev = cur
            cur = cur.next
        }
        else
        {
            cur.next = cur.next.next
        }
    }

    return listHead
}