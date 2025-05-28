def reverseQueue( q):
    if q.empty():
        return q
    item = q.get()
    reverseQueue(q)
    q.put(item)
    return q