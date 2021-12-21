import sys
sys.stdin = open("input.txt")

from collections import deque

row, col = map(int, input().split())
matrix = [list(map(str, input())) for _ in range(row)]
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

"""
기본 로직은 L을 기준으로 bfs를 하여 최대 값을 찾는다
"""
def bfs(x, y):
    global cnt
    queue = deque()
    # x, y, cnt = 0을 추가
    queue.append((x, y, 0))
    visited = [[False] * col for _ in range(row)]
    visited[x][y] = True

    while queue:
        x, y, c = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 제한
            if 0 <= nx < row and 0 <= ny < col:
                # L이거나 방문하지 않을 경우만 움직이면서 개수 체크
                if matrix[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, c+1))
                    cnt = c + 1

    return cnt

cnt = 0
ans = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] == 'L':
            # 그중에서 최댓값 출력
            ans = max(ans, bfs(i, j))

print(ans)