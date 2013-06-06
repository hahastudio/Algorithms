from math import log, e, pi

def FFT(A,w):
	"""Input: An tuple or list A=(a_0, a_1,..., a_n-1), for n a power of 2
	A primitive nth root of unity, w
	Output: M_n(w)*A
	"""
	if abs(w-1) < 0.0001:
		return A
	n = len(A)
	s = FFT(A[::2], w**2)
	s1 = FFT(A[1::2],w**2)
	r = [0] * n
	for i in xrange(n/2):
		t = pow(w, i) * s1[i]
		r[i] = s[i] + t
		r[i+n/2] = s[i] - t
	return r

class Polynomial(object):
	"""Polynomial(iterable real number sequence) -> new Polynomial initialized from iterable's items
	"""
	def __init__(self, A, degree = 0):
		"""Given a arbitrary length iterable's items, make a Polynomial A(x) of degree <= n-1, where n is a power of 2.
		"""
		n = len(A)
		self.degree = n-1 if n-1 >= degree else degree
		self.a = [0] * (self.degree + 1)
		self.a[:n] = A[:]

	def __mul__(self, p):
		log2 = log(self.degree + p.degree + 2, 2)
		degree = pow(2, int(log2 if log2-int(log2)<0.000001 else log2+1)) - 1
		p1 = Polynomial(self.a, degree)
		p2 = Polynomial(p.a, degree)
		w = e ** (2 * pi * 1j / (degree + 1))
		f1 = FFT(p1.a, w)
		f2 = FFT(p2.a, w)
		fc = [i[0]*i[1] for i in zip(f1, f2)]
		c = [abs(i/(degree+1)) if i.real>0 else -abs(i/(degree+1)) for i in FFT(fc, w.conjugate())]
		c = [i if abs(i) > 1e-5 else 0 for i in c]
		n = len(c)
		for i in c[::-1]:
			if not i:
				n -= 1
		c = c[:n] or (0,)
		return Polynomial(c)

	def __repr__(self):
		if self.degree < 0:
			return
		s = str(self.a[0])
		if self.degree >= 1:
			s += " + " + str(self.a[1]) + 'x'
		if self.degree > 1:
			s += " + " + " + ".join(str(i[1]) + "x^" + str(i[0]+2) for i in enumerate(self.a[2:]))
		return s
