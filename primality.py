import math
import random
from modular_arithmetic import modexp

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
            if modexp(a, n - 1, n) != 1:
                return False
        return True
    else:
        for i in xrange(100):
            a = random.randint(2, n - 1)
            if modexp(a, n - 1, n) != 1:
                return False
        return True


    
