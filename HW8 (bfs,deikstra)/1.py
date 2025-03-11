N,S,F = list(map(int,input().split()))
graph = {}
for i in range(1, N + 1):
    x = list(map(int,input().split()))
    graph[i] = []
    for j in range(N):
        if  x[j] != -1:
            graph[i].append((j + 1, x[j])) # вершина и вес


costs = {i: float('inf') for i in range(1, N + 1)}  # Все расстояния бесконечны
costs[S] = 0  # Расстояние до стартовой вершины = 0

parents = {i: None for i in range(1, N + 1)}
visited = [0] * (N+1)

# print(graph)
# print(costs)

def find_lowest_cost_node(costs): # если закончились непосещенные вершины - выыводит None
    lowest_cost = float('inf') # минимальный вес
    lowest_cost_node = None # вершина с мин СТОИМОСТЬЮ
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and not visited[node]:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def Deikstra(graph):
    node = find_lowest_cost_node(costs)
    while node is not None:
        visited[node] = 1
        cost = costs[node]
        for sosed,price in graph[node]: # тут кортеж, надо распаковать
            new_cost = cost + price
            if new_cost < costs[sosed]:
                costs[sosed] = new_cost
                parents[sosed] = node

        node = find_lowest_cost_node(costs)

    if costs[F] == float('inf'):
        return (-1)

    return costs[F]


print(Deikstra(graph))
