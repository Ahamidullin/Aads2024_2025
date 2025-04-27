from collections import deque
n, m = list(map(int,input().split()))
matrix = [list(map(int,input().split())) for i in range(n)]
# print(matrix)

distance = [[float('inf') for i in range(m)] for j in range(n)]
# print(distance)

# проходимся по матрице и добалвяем в очерерь все с единицами
# будем запускать BFS от всех клеток которые единицы
deq = deque()
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            distance[i][j] = 0 # будем идти от них => расстояния = 0
            deq.append([i,j]) # добавляет справа

# print(deq)

# ОБЩАЯ ИДЕЯ: добавляем все справа, выводим из очереди слева
# поебашили:
while deq:
    # current = deq.pop() # удаляет правый
    current = deq.popleft() # удовлетворяет принципу FIFO || НАШ РОДИТЕЛЬ
    # print(current)

    directions = [(1,0),(0,1),(-1,0),(0,-1)] # нужно для прохода соседей

    for x,y in directions:
        new_x = x + current[0]
        new_y = y + current[1]
        # print(new_x,new_y)

        if 0 <= new_x < n and 0 <= new_y < m and  distance[new_x][new_y] == float("inf"):
            #distance[new_x][new_y] += 1 # +1 всегда потому что родители всегда с 1|| inf + 1 = inf поэтому делаем так:
            distance[new_x][new_y] = distance[current[0]][current[1]] + 1# расстояние до ребенка = соседа это расстояние от родителя + 1

            deq.append([new_x,new_y]) # теперь в будущем она сама будет родителем

for row in distance:
    print(*row)





