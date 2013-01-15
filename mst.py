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