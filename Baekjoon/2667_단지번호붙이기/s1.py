import sys
sys.stdin = open("input.txt")

def bfs(x, y):
    cnt = 1
    q = [(x, y)]
    visited[x][y] = 1

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and arr[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    result.append(cnt)

# 상우하좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            bfs(i, j)

result.sort()
print(len(result))
for i in result:
    print(i)