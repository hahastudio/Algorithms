import math

def fib1(n):
    """Return the nth Fibinacci number, implemented by the recursive definition.
    It's an exponential algorithm.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)

def fib2(n):
    """Return the nth Fibinacci number, implemented by the iterative definition.
    It's a polynomial algorithm.
    """
    if n == 0:
        return 0
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a + b
    return a

def fib3(n):
    """Return the nth Fibinacci number, implemented by the formula.
    It's a nearly constant-time algorithm.
    However, it has a poor precise. When calculating fib3(72), it starts to become wrong.
    """
    sq5 = math.sqrt(5)
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5))
