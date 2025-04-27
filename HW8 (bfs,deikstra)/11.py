
n, s, f = map(int, input().split())
# переебашиваем в 0 индексовую систему
s -= 1
f -= 1

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# print(matrix)

distance = [float('inf') for i in range(n)]
parents = [None for i in range(n)]
visited = [False for i in range(n)]

# На каждой итерации Дейкстры вы выбираете глобально самую "дешёвую"
# необработанную вершину, а не ограничиваетесь соседями текущей.
# Обновление расстояний до соседей происходит уже в основном цикле, а не в функции поиска

distance[s] = 0
def find_lowest_node():
    # visited[current] = True
    min_distance= float('inf')
    nex_node = None

    for i in range(n):
        if visited[i] == False :

            if distance[i] < min_distance:
                min_distance =  distance[i]
                nex_node = i

    return nex_node

# проверить существует ли более дешевый путь к соседям этого узла, и если сущ. обновить их стоимости

now = find_lowest_node() # самый дешевый глобальный путь

while now is not None: # если просто current то при corrent = 0 это false
    visited[now] = True

    for i in range(len(matrix[now])):
        if matrix[now][i] >= 0 and not visited[i]:
            if distance[now] + matrix[now][i] < distance[i]:
                distance[i] = distance[now] + matrix[now][i]
                parents[i] = now

    now = find_lowest_node()




if distance[f] == float('inf'):
    print(-1)
else:
    path = []
    current = f
    while current is not None:
        path.append(current + 1)
        current = parents[current]

    path.reverse()
    print(*path)




















