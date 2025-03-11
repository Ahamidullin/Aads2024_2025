# f = open('input.txt')
# num = int(f.readline())
# print(num)

num = int(input())

for k in range(num):
    n, m = [int(x) for x in input().split()]
    gr = [[] for i in range(n)]
    for i in range(m):
        u, v, w = [int(x) for x in input().split()]
        gr[u].append((v,w))
        gr[v].append((u,w))

    start = int(input())
    dist = [float("inf")] * n
    dist[start] = 0
    q = dict()
    q[start] = 0

    while q:
        cur_vertex = 1
        cur_weight = float('inf')
        for key, value in q.items():
            if value < cur_weight:
                cur_vertex = key
                cur_weight = value

        q.pop(cur_vertex)
        for to, w in gr[cur_vertex]:
            if dist[cur_vertex] + w < dist[to]:
                q[to] = dist[cur_vertex] + w
                dist[to] = dist[cur_vertex] + w
print(*dist)
