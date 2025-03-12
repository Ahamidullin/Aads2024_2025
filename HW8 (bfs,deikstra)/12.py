import sys
import heapq

def solve():
    INF = 10**15
    NUM = int(input())
    outputs = []
    for _ in range(NUM):
        N, M = map(int, input().split())
        graph = [[] for _ in range(N)]
        for __ in range(M):
            u, v, w = map(int, input().split())
            graph[u].append((v, w))
            graph[v].append((u, w))
        start = int(input())
        dist = [INF]*N
        dist[start] = 0
        heap = [(0, start)]
        while heap:
            cur_dist, u = heapq.heappop(heap)
            if cur_dist > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))
        res = []
        for d in dist:
            if d == INF:
                res.append("2009000999")
            else:
                res.append(str(d))
        outputs.append(" ".join(res))
    print("\n".join(outputs))


solve()
