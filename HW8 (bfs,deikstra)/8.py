from collections import deque
n, m, s = map(int, input().split())
#
# # Инициализируем матрицу смежности n x n, заполненную нулями
# matrix = [[0] * n for _ in range(n)]
#
# # Заполняем матрицу на основе рёбер
# for _ in range(m):
#     u, v = map(int, input().split())
#     # Учитываем 1-based индексацию, переводим в 0-based
#     u -= 1
#     v -= 1
#     matrix[u][v] = 1
#     matrix[v][u] = 1
#
# print(matrix)



adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, vi = map(int, input().split())
    adj[u].append(vi)
    adj[vi].append(u)

print(adj)
path = [s]

visited = [False for i in range(n + 1)]
deq = deque()
deq.append(s) # вершины с 1
visited[s] = True
while deq:
    current = deq.popleft()

    for i in adj[current]: # соседи
        # print(i)
        if not visited[i]:
            visited[i] = True
            deq.append(i)
            path.append(i)


print(len(path))
print(*path)




