import sys
sys.stdin = open("input.txt")

from collections import deque

# 상 하 좌 우 우상 우하 좌상 좌하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        # 8 방향에 대해 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 벽인 조건 + 방문처리가 안된 지점
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == False:
                if matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    else:
        matrix = [list(map(int, input().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 1 and visited[i][j] == False:
                    bfs(i, j)
                    cnt += 1
        print(cnt)
