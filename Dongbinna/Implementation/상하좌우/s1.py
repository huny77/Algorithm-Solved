import sys
sys.stdin = open("input.txt")

n = int(input())
plans = input().split()
x, y = 1, 1

# 좌 우 상 하
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move = ['L', 'R', 'U', 'D']

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
move = ['U', 'R', 'D', 'L']

for plan in plans:
    # 이동 후 4방향에 대한 좌표 구하기
    for i in range(4):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간이 벗어나는 경우 무시
    if not (1 <= nx < n and 1 <= ny < n):
        continue

    # if nx < 1 or ny < 1 or nx > n or ny >n:
    #     continue

    # 이동
    x, y = nx, ny

print(x, y)