import math
import random

def primality1(n):
    """give a positive integer n, testing primality.
    It proclaim n a prime as soon as it have rejected all candidate up to sqrt(n).
    """
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primality2(n):
    """give a positive integer n, testing primality.
    With the power of Fermat's little theorem, we can use a probabilistic tests
    that it makes the probability of failure at most 2^(-100).
    """
    if n <= 102:
        for a in xrange(2, n):
            if pow(a, n - 1, n) != 1:
                return False
        return True
    else:
        for i in xrange(100):
            a = random.randint(2, n - 1)
            if pow(a, n - 1, n) != 1:
                return False
        return True


def generate_prime(n):
    """Return a n-bit prime."""
    while 1:
        p = random.randint(pow(2, n-2), pow(2, n-1)-1)
        p = 2 * p + 1
        if primality2(p):
            return p


