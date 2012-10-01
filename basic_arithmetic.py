def multiply(x, y):
    """requires two n-bit integers x & y, where y >= 0
    Al Khwarizmi's algorithm to multiply two number x and y.
    Return their product.
    """
    if x == 0 or y == 0:
        return 0
    z = multiply(x, y / 2)
    if y % 2 == 0:
        return 2 * z
    else:
        return x + 2 * z

def divide(x, y):
    """requires two n-bit integers x & y, where y >= 1
    Return the quotient and remainder of x divided by y
    """
    if x == 0:
        return 0, 0
    q, r = divide(x / 2, y)
    q, r = 2 * q, 2 * r
    if x % 2 != 0:
        r += 1
    if r >= y:
        r -= y
        q += 1
    return q, r

def multiply2(x, y):
    """requires two n-bit positive integers x & y,
    return their product.
    Using Gauss's idea in divide-and-conquer algorithm."""
    xB, yB = bin(x)[2:], bin(y)[2:]
    xN, yN = len(xB), len(yB)
    n = max(xN, yN)
    if xN > yN:
        yB = '0' * (xN - yN) + yB
    if yN > xN:
        xB = '0' * (yN - xN) + xB
    if n == 1:
        return x * y
    xL, xR = int(xB[:-(n/2)] or '0', 2), int(xB[-(n/2):] or '0', 2)
    yL, yR = int(yB[:-(n/2)] or '0', 2), int(yB[-(n/2):] or '0', 2)
    p1 = multiply2(xL, yL)
    p2 = multiply2(xR, yR)
    p3 = multiply2(xL+xR, yL+yR)
    return p1 * pow(2, n/2*2) + (p3 - p1 - p2) * pow(2, n/2) + p2
