"""
约定：图的存储方法
这里的图采用邻接表的方法存储。有两种可行的方式：
1. 边无权重：
采用集合存储该点可到达的点集
2. 边有权重：
采用字典(点:边的权重)存储该点可到达的点集
例：
V = a, b, c, d, e, f, g, h = range(8)
E = [
	set([b, c, f]),
	set([e]),
	set([d]),
	set([a, h]),
	set([f, g, h]),
	set([b, g]),
	set(),
	set([g])
	]
G = (V, E)
"""
from collections import deque

inf = float("inf")

def bfs(G, s):
	"""Input: Graph G = (V, E), directed or undirected; vertex s in V
	Output: For all vertices u reachable from s, dist[u] is set to the
		distance from s to u
	"""
	V, E = G
	dist = [inf for u in V]
	dist[s] = 0
	Q = deque([s])
	while Q:
		u = Q.popleft()
		for v in E[u]:
			if dist[v] == inf:
				Q.append(v)
				dist[v] = dist[u] + 1
	return dist