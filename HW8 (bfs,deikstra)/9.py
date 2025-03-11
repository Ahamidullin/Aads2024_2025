from collections import deque

n, m = map(int, input().split())
maze = [input() for _ in range(m)]
start = None
cnt = 0 # кол - во вершин в дереве
for i in range(m):
    for j in range(n):
        if maze[i][j] == '.':
            cnt += 1
            if start is None:
                start = (i, j)


def BFS(sx, sy):
    dist = [[-1]*n for _ in range(m)]
    dist[sx][sy] = 0
    q = deque([(sx, sy)])
    fx, fy = sx, sy
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n:
                if maze[nx][ny]=='.' and dist[nx][ny]==-1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    if dist[nx][ny] > dist[fx][fy]:
                        fx, fy = nx, ny
    return fx, fy, dist[fx][fy]

x1, y1, _ = BFS(*start)
x2, y2, d = BFS(x1, y1)
print(d)
