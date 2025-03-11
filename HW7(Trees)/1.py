
# n = int(input())
# matrix = [list(map(int,input().split())) for i in range(n)]
# visited = [False for i in range(n)]
# current = 0
# def dfs(matrix,visited,current):
#     visited[current] = True
#     print(f"Вершина {current + 1} имеет соседей:", end = '')
#
#     for i in range(len(matrix[current])): # выводим всех соседей
#         if matrix[current][i]:
#             print(i + 1)
#
#     for i in range(len(matrix[current])):
#         if not (visited[i]) and matrix[current][i] :
#             dfs(matrix,visited,i)
#
# print(dfs(matrix,visited,current))

# def dfs(matrix,visited,current):
#
#     if not visited[current]:
#         print(f"текущая вершина {current + 1} имеет соседей:")
#         visited[current] = True
#
#
#
#         for i in range(len(matrix[current])): #индексы потенциальных соседей
#             if matrix[current][i] == 1 and (not visited[i]): # находим соседа
#                 print(i+1)
#                 dfs(matrix,visited,i) # не matrix[current][i] - это 0 или 1, нам нужен индекс





# Ты передаёшь параметр current (текущая вершина), но нигде его не используешь.
# В DFS нужно начинать обход с текущей вершины и смотреть её соседей, а не перебирать все вершины в цикле for i in range(n).ъ

# 5
# 0 1 1 0 0
# 1 0 1 0 0
# 1 1 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0

n, k = list(map(int,input().split()))
matrix = [list(map(int,input().split())) for i in range(n)]
visited = [False for i in range(n)]
current = k - 1

def dfs(matrix,visited,current):
    cnt = 1 # берем саму вершину
    visited[current] = True

    for i in range(len(matrix[current])): # проходим по всем соседям
        if matrix[current][i] and not visited[i]:
            cnt += dfs(matrix, visited, i)

    return cnt


print(dfs(matrix,visited,current))