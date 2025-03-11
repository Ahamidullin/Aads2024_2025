from collections import deque

n, m = list(map(int, input().split()))
matrix = [[int(x) for x in input().split()] for i in range(n)]

x_st, y_st = [int(i) - 1 for i in input().split()]
x_fin, y_fin = [int(i) - 1 for i in input().split()]

start = (y_st, x_st)
finish = (y_fin, x_fin)

distance = [[float('inf') for i in range(m)] for j in range(n)]

deq = deque()
deq.append(start)
distance[y_st][x_st] = 0

while deq:
    current = deq.popleft()
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for x, y in directions:
        # current[0] – строка, current[1] – столбец
        new_x, new_y = current[0] + x, current[1] + y
        #  0 <= строка < n и 0 <= столбец < m
        if (0 <= new_x < n and 0 <= new_y < m and matrix[new_x][new_y] != 1 and distance[new_x][new_y] == float('inf')):
            distance[new_x][new_y] = distance[current[0]][current[1]] + 1
            deq.append((new_x, new_y))

if distance[finish[0]][finish[1]] == float('inf'):
    print(-1)
else:
    print(distance[finish[0]][finish[1]])

