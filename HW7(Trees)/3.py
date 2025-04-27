

n, m = map(int, input().split())

def is_tree(n,m):
    if m != n - 1:
        return False

    graph = {i: [] for i in range(1,n+1)}
    visited = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # print(graph)

    def dfs(parent, current):
        visited[current] = 1

        for neighbor in graph[current]:
            if neighbor == parent:
                continue
            if visited[neighbor] == 1:
                return False
            if not dfs(current,neighbor):
                return False

        return True

    if not dfs(-1,1):
        return False

    return sum(visited) == n


print("YES" if is_tree(n, m) else "NO")



# print(graph)




