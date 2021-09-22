import sys
sys.stdin = open("input.txt")

def bfs(x, y):
    q = [(x, y)]
    visited[x][y] = 1
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m): continue
            if arr[nx][ny] == 0: continue
            if arr[nx][ny] == 1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))
    return arr[n-1][m-1]


# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
print(bfs(0, 0))