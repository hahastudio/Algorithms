from math import log

def multiply(x, y):
    """requires two n-bit integers x & y, where y >= 0
    Al Khwarizmi's algorithm to multiply two number x and y.
    Return their product.
    """
    if x == 0 or y == 0:
        return 0
    z = multiply(x, y>>1)
    if y & 1 == 0:
        return z<<1
    else:
        return x + (z << 1)

def divide(x, y):
    """requires two n-bit integers x & y, where y >= 1
    Return the quotient and remainder of x divided by y
    """
    if x == 0:
        return 0, 0
    q, r = divide(x>>1, y)
    q, r = q<<1, r<<1
    if x & 1 == 1:
        r += 1
    if r >= y:
        r -= y
        q += 1
    return q, r

def multiply2(x, y):
    """requires two n-bit positive integers x & y,
    return their product.
    Using Gauss's idea in divide-and-conquer algorithm."""
    n = int(max(log(x or 1, 2), log(y or 1, 2))) + 1
    if n == 1:
        return x * y
    xL, xR = x>>(n>>1), x & ((1<<(n>>1)) - 1)
    yL, yR = y>>(n>>1), y & ((1<<(n>>1)) - 1)
    p1 = multiply2(xL, yL)
    p2 = multiply2(xR, yR)
    p3 = multiply2(xL+xR, yL+yR)
    return (p1 << ((n >> 1) << 1)) + ((p3 - p1 - p2) << (n >> 1)) + p2
