from binary_heap import binary_heap

class dset(object):
	"""A data structure for disjoint sets."""
	def __init__(self, n):
		self.parent = range(n)
		self.rank = [0] * n

	def __len__(self):
		return len(self.parent)

	def union(self, x, y):
		rx = self.find(x)
		ry = self.find(y)
		if rx == ry:
			return
		if self.rank[rx] > self.rank[ry]:
			self.parent[ry] = rx
		else:
			self.parent[rx] = ry
			if self.rank[rx] == self.rank[ry]:
				self.rank[ry] += 1

	def find(self, x):
		if x != self.parent[x]:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

"""
I've changed the way to save a graph.
G = (V ,E); which for example:
V = a, b, c, d, e, f = range(6)
E = {
	(a, b):2,
	(a, c):1,
	(b, c):2,
	(b, d):1,
	(c, d):2,
	(c, e):3,
	(d, e):3,
	(d, f):4,
	(e, f):1
	}
"""

def kruskal(G):
	"""Input: A connected undirected graph G=(V, E) with edge weights
Output: A minimum spanning tree defined by the edges X
	"""
	V , E = G
	d = dset(len(V))
	X = set([])
	E_sorted = list(sorted(E, key=lambda k:E[k]))
	for u, v in E_sorted:
		if d.find(u) != d.find(v):
			X.add((u, v))
			d.union(u, v)
	return X

def prim(G):
	"""Input: A connected undirected graph G=(V, E) with edge weights
Output: A minimum spanning tree defined by the dict prev
	"""
	V, E = G
	cost = {}
	prev = {}
	for u in V:
		cost[u] = float("inf")
		prev[u] = None
	cost[V[0]] = 0
	H = binary_heap(V, key=lambda u:cost[u])
	while len(H):
		v = H.deletemin()
		for z in E[v]:
			weightVZ = E[v][z]
			if cost[z] > weightVZ and z in H.h[1:len(H)+1]:
				cost[z] = weightVZ
				prev[z] = v
				H.decreasekey(z)
	return prev

if __name__ == '__main__':
	V = a, b, c, d, e, f = range(6)
	E = {
		a: {b:5, c:6, d:4},
		b: {a:5, c:1, d:2},
		c: {a:6, b:1, d:2, e:5, f:3},
		d: {a:4, b:2, c:2, f:4},
		e: {c:5, f:4},
		f: {c:3, d:4, e:4}
	}
	G = (V, E)
	print prim(G)
