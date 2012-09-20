def Euclid(a, b):
    """Two integers a & b with a >= b >= 0
    Euclid's algorithm for finding the greatest common divisor of two numbers.
    """
    if b == 0:
        return a
    return Euclid(b, a % b)

def extended_Euclid(a, b):
    """Two integer a & b with a >= b >= 0
    Return integers x, y, d such that d = Euclid(a, b) and a*x + b*y = d
    """
    if b == 0:
        return 1, 0, a
    x1, y1, d = extended_Euclid(b, a % b)
    return y1, x1 - a / b * y1, d

