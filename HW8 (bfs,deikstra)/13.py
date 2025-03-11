n = int(input())
dist = [float('inf')] * (n + 1)
dist[1] = 0
for i in range(1, n):
    for j in range(i + 1, n + 1):
        wt = (179 * i + 719 * j) % 1000 - 500
        dist[j] = min(dist[j], dist[i] + wt)
print(dist[n])