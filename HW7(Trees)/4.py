import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

def find_cycle(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    color = [0] * (n + 1)
    parent = [-1] * (n + 1)

    cycle_start = -1
    cycle_end = -1

    def dfs(node): # проверка того есть ли циклы
        nonlocal cycle_start, cycle_end # find_cycle может править эти переменные
        color[node] = 1 # еше не проверили всех детей, но мы в этой вершине
        for neighbor in graph[node]:
            if color[neighbor] == 0:
                parent[neighbor] = node
                if dfs(neighbor):
                    return True
            elif color[neighbor] == 1:
                cycle_start = neighbor
                cycle_end = node
                return True
        color[node] = 2 # прошлись по ним и по их детям
        return False

    for v in range(1, n + 1):
        if color[v] == 0:
            if dfs(v):
                break

    if cycle_start == -1:
        print("NO")
        return

    cycle = []
    cycle.append(cycle_start)
    v = cycle_end

    while v != cycle_start:
        cycle.append(v)
        v = parent[v]
    cycle.append(cycle_start)
    cycle.reverse()

    print("YES")
    print(*cycle[:-1])

n, m = map(int, input().split())
edges = [[int(j) for j in input().split()] for i in range(m)]
find_cycle(n, edges)

