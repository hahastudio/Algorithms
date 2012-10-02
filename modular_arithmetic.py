from euclid import extended_Euclid

def modexp(x, y, N):
    """Two n-bit integers x & N, an integer exponent y
    Return x^y % N
    """
    if y == 0:
        return 1
    z = modexp(x, y>>1, N)
    if y & 1 == 0:
        return z * z % N
    else:
        return x * z * z % N

def modinv(a, N):
    """Two n-bit integers a & N
    Return the multiplicative inverse of a modulo N if it exists, else NaN
    """
    x, y, d = extended_Euclid(a, N)
    if d == 1:
        return x % N
    else:
        return float("nan")
