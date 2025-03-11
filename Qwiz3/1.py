# n = int(input())
# g = []
# for i in range(n):
#     g.append([int(x) for x in input().split()])
#
# cnt = 0
# ans = []
# for i in range(len(g)):
#     for j in range(i + 1):
#         if g[i][j] == 1:
#             print(j + 1, i + 1)

x = list(map(int,input().split()))
ans = []
for i in range(x[1]):
    ans.append(list(map(int,input().split())))

# print(ans)
matrix = [[0 for _ in range(x[0])] for _ in range(x[0])]
# print(matrix)

cnt = 0

for i in ans:
    a,b = i
    matrix[a - 1][b - 1] = 1
    matrix[b - 1][a - 1] = 1

# print(matrix)

for i in matrix:
    print(*i)
# print(matrix)









