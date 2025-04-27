import heapq

n = int(input())
a, b = map(int, input().split())
k = int(input())

flights = []
for _ in range(k):
    u, t_dep, v, t_arr = map(int, input().split())
    flights.append((u, t_dep, v, t_arr))

INF = 10**18
dist = [INF] * (n + 1)
dist[a] = 0

pq = [(0, a)]

graph = [[] for _ in range(n + 1)]
for u, t_dep, v, t_arr in flights:
    graph[u].append((t_dep, v, t_arr))

while pq:
    t_curr, u = heapq.heappop(pq)
    if t_curr > dist[u]:
        continue
    for t_dep, v, t_arr in graph[u]:
        if t_dep >= t_curr and t_arr < dist[v]:
            dist[v] = t_arr
            heapq.heappush(pq, (t_arr, v))

print(dist[b])