from heapq import heappop, heappush

inf = float("inf")

def relax(W, u, v, D, P):
    d = D.get(u,inf) + W[u][v] # Possible shortcut estimate
    if d < D.get(v,inf): # Is it really a shortcut?
        D[v], P[v] = d, u # Update estimate and parent
    return True# There was a change!

def Dijkstra(G, s):
    D, P, Q, S = {s:0}, {}, [(0,s)], set() # Est., tree, queue, visited
    while Q: # Still unprocessed nodes?
        _, u = heappop(Q) # Node with lowest estimate
        if u in S: continue # Already visited? Skip it
        S.add(u) # We've visited it now
        for v in G[u]: # Go through all its neighbors
            relax(G, u, v, D, P) # Relax the out-edge
            heappush(Q, (D[v], v)) # Add to queue, w/est. as pri
    return D, P# Final D and P returned

def Bellman_Ford(G, s):
    """Input: Directed graph G=(V, E) with no negative cycles;
    vertex s in V
Output: For all vertices u reachable from s, dist(u) is set to the 
    distance from s to u;
    prev(u) is set to the previous vertex reaches u in the shortest path.
    """
    size = len(G)
    dist = [inf] * size
    prev = [None] * size
    dist[s] = 0
    for i in xrange(size - 1):
        for u, e in enumerate(G):
            for v in e:
                l = dist[u] + e[v]
                if dist[v] > l:
                    dist[v] = l
                    prev[v] = u
    return dist, prev

