from collections import deque
n, m = map(int, input().split())
city = [0] + list(map(int, input().split()))

graph = [[] for i in range(n+1)]

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)

parents = [None for i in range(n+1)]
distance = [float('inf') for i in range(n+1)]

start = 1
distance[start] = 0
deq = deque([start])

while deq:
    current = deq.popleft()

    for i in graph[current]:
        if city[current] != city[i]:
            cost = 1
        else: cost = 0

        new_dist = distance[current] + cost

        if new_dist < distance[i]:
            distance[i] = new_dist
            parents[i] = current
            deq.append(i)

if distance[n] == float('inf'):
    print("impossible")
else:

    path = []
    current = n
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()

    print(distance[n], len(path))
    print(*path)