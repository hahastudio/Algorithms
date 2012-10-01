from collections import deque

def mergesort(lst):
    """Input a list of numbers, return a sorted version."""
    n = len(lst)
    if n > 1:
        return merge(mergesort(lst[:n/2]), mergesort(lst[n/2:]))
    else:
        return lst

def merge(x, y):
    if not isinstance(x, list):
        x = [x]
    if not isinstance(y, list):
        y = [y]
    k, l = len(x), len(y)
    if k == 0:
        return y
    if l == 0:
        return x
    if x[0] <= y[0]:
        return [x[0]] + merge(x[1:], y)
    else:
        return [y[0]] + merge(x, y[1:])

def iterative_mergesort(lst):
    Q = deque()
    for item in lst:
        Q.append(item)
    while len(Q) > 1:
        Q.append(merge(Q.popleft(), Q.popleft()))
    return Q.popleft()
