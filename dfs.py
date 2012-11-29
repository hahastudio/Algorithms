"""
第3章里面的DFS就是个概念模型，没有输出= =用不来的= =
因此这部分按照《Python Algorithms》介绍的方法来。
顺带一提，《Python Algorithms》是本好书= =
约定：图的存储方法
这里的图采用邻接表的方法存储。有两种可行的方式：
1. 边无权重：
采用集合存储该点可到达的点集
2. 边有权重：
采用字典(点:边的权重)存储该点可到达的点集
例：
a, b, c, d, e, f, g, h = range(8)
G = [
	set([b, c, f]),
	set([e]),
	set([d]),
	set([a, h]),
	set([f, g, h]),
	set([b, g]),
	set(),
	set([g])
	]
"""
def rec_dfs(G, s, S=None):
	if S is None:
		S = set()
	S.add(s)
	for u in G[s]:
		if u in S:
			continue
		rec_dfs(G, u, S)

def iter_dfs(G, s):
	S, Q = set(), []
	Q.append(s)
	while Q:
		u = Q.pop()
		if u in S:
			continue
		S.add(u)
		Q.extend(G[u])
		yield u

def dfs(G, s, pre, post, S=None, t=0):
	if S is None:
		S = set()
	pre[s] = t
	t += 1
	S.add(s)
	for u in G[s]:
		if u in S:
			continue
		t = dfs(G, u, pre, post, S, t)
	post[s] = t
	t += 1
	return t