from euclid import Euclid
from modular_arithmetic import modinv
from primality import generate_prime

class RSA(object):
    def __init__(self, n=256):
        """Generate n-bit prime p, q
        Initialize N=pq, e, d
        """
        self.p = generate_prime(n)
        self.q = generate_prime(n)
        self.N = self.p * self.q
        self.u = (self.p - 1) * (self.q - 1)
        self.e = 3
        while Euclid(self.e, self.u) != 1:
            self.e += 2
        self.d = modinv(self.e, self.u)
    def encrypt(self, msg):
        """encrypt the message, return a list of encoded message."""
        encode_list = [pow(ord(c), self.e, self.N) for c in msg]
        return encode_list
    def decrypt(self, enc):
        """decrypt the list of encoded message."""
        decode_list = [pow(i, self.d, self.N) for i in enc]
        return "".join(unichr(i) for i in decode_list)
