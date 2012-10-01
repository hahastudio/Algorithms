import random

class UniHashing(object):
    def __init__(self, length=100, p=1733):
        """length is the 
        Initialize the group of hash functions"""
        self.length = length
        self.p = p
        self.lst = [ [] for i in xrange(length)]
        self.func = [tuple(random.randint(0, length-1) for j in xrange(8))
                     for i in xrange(p)]

    def calc_key(self, data, key=None):
        def cut(n):
            r = [0] * 8
            q = n
            for i in xrange(7):
                q, r[7-i] = divmod(q, 256)
            r[0] = q
            return tuple(r)
        if key is not None:
            x = cut(key)
            a = self.func[key % self.p]
        else:
            x = cut(data)
            a = self.func[data % self.p]
        h = sum(i*j for i, j in zip(x, a)) % self.length
        return h

    def insert(self, data, key=None):
        h = self.calc_key(data, key)
        self.lst[h].append(data)

    def hasdata(self, data, key=None):
        h = self.calc_key(data, key)
        if data in self.lst[h]:
            return True
        else:
            return False
    
    def remove(self, data, key=None):
        h = self.calc_key(data, key)
        self.lst[h].remove(data)
