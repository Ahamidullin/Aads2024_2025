n, m = [int(x) for x in input().split()]

edges = []

for i in range(m):
    u, v, w = [int(x) for x in input().split()]
    edges.append((u, v, w))

edges = sorted(edges, key=lambda x: x[2])

p = [-1] * (n + 1)


def find(v):
    r = v
    while p[r] != -1:
        r = p[r]
    while p[v] != -1:
        t = p[v]
        p[v] = r
        v = t
    return r


def union(v, u):
    p[find(v)] = find(u)


ans = []
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        ans.append((u, v, w))

# print(*ans, sep='\n')
print(sum(e[2] for e in ans))