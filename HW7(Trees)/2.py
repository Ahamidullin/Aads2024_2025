n, m = map(int, input().split())
graph = {i: [] for i in range(1,n+1)}

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)

visited = [False] * (n + 1)

comp_id = [0] * (n+1)
current = next(iter(graph))


def dfs(start, comp_num):
    stack = [start]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            comp_id[current] = comp_num
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)




comp_num = 0
for i in range(1, n + 1): # проход по вершинам
    if not visited[i]:
        comp_num +=1
        dfs(i,comp_num)




print(comp_num)
print(" ".join(map(str, comp_id[1:])))




#
# def dfs(vertex, component_number):
#     visited[vertex] = True  # Используем глобальный visited
#     comp_id[vertex] = component_number
#     for neighbor in graph[vertex]:  # Используем глобальный graph
#         if not visited[neighbor]:
#             dfs(neighbor, component_number)
#
# component_count = 0
# for vertex in range(1, n + 1):
#     if not visited[vertex]:
#         component_count += 1
#         dfs(vertex, component_count)  # Теперь работает с двумя аргументами
#
# print(component_count)
# print(" ".join(map(str, comp_id[1:])))