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
