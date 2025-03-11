n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

INF = float('inf')
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == -1:
            dist[i][j] = INF
        else:
            dist[i][j] = graph[i][j]
    dist[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

diameter = 0
eccentricities = []
for i in range(n):
    max_dist = 0
    for j in range(n):
        if dist[i][j] != INF:
            max_dist = max(max_dist, dist[i][j])
    eccentricities.append(max_dist)
    diameter = max(diameter, max_dist)

radius = min(eccentricities)

print(diameter)
print(radius)