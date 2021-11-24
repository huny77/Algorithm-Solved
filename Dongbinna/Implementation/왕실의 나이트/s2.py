import sys
sys.stdin = open("input.txt")

# 나이트가 이동할 수 있는 8가지 방향 정의
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

# 현재 나이트의 위치 입력 받기
data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

ans = 0
for i in range(8):
    # 이동하고자 하는 위치 확인
    next_row = row + dx[i]
    next_col = col + dy[i]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        ans += 1

print(ans)