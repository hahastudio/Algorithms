from math import ceil

class binary_heap(object):
	"""docstring for binary_heap"""
	def __init__(self, S, key=lambda x:x):
		self.h = [None]
		self.key = key
		self.length = len(S)
		for x in S:
			self.h.append(x)
		for i in xrange(len(S), 0, -1):
			self.siftdown(self.h[i], i)
	def __len__(self):
		return self.length
	def siftdown(self, x, i):
		"""place element x in position i of h, and let it sift down"""
		c = self.minchild(i)
		#print "minchild", c, i
		while c != 0 and self.key(self.h[c]) < self.key(x):
			self.h[i] = self.h[c]
			i = c
			c = self.minchild(i)
		self.h[i] = x
	def minchild(self, i):
		"""return the index of the smallest child of h[i]"""
		if 2 * i > len(self):
			return 0
		else:
			uprange = min(len(self), 2*i+1)
			minkey = float("inf")
			minpos = 0
			for j in xrange(2*i, uprange+1):
				if self.key(self.h[j]) < minkey:
					minkey = self.key(self.h[j])
					minpos = j
			return minpos
	def insert(self, x):
		self.h.append(0)
		self.length += 1
		self.bubbleup(x, len(self))
	def decreasekey(self, x):
		#print "bubbleup", self.h, self.length
		self.bubbleup(x, self.h.index(x))
	def deletemin(self):
		if len(self):
			x = self.h[1]
			#print "end:", self.h[len(self)]
			#self.h[1] = self.h[len(self)]
			#print self.h
			#print self.h
			self.siftdown(self.h[len(self)], 1)
			self.length -= 1
			return x
		else:
			return None
	def bubbleup(self, x, i):
		"""place element x in position i of h, and let it bubble up"""
		p = int(ceil(i/2.0))
		#print "p=%d" % p
		while i != 1 and self.key(self.h[p]) > self.key(x):
			self.h[i] = self.h[p]
			i = p
			p = int(ceil(i/2.0))
			#print "p=%d" % p
		self.h[i] = x

if __name__ == '__main__':
	s = [1]
	bh = binary_heap(s)
	print bh.h
	bh.insert(3)
	bh.insert(5)
	bh.insert(2)
	bh.insert(4)
	bh.insert(6)
	print bh.h
	print bh.deletemin(), bh.h
	print bh.deletemin(), bh.h
	print bh.deletemin(), bh.h
	print bh.deletemin(), bh.h
	print bh.deletemin(), bh.h
	print bh.deletemin(), bh.h
	bh.insert(2)
	bh.insert(1)
	print bh.h
	
