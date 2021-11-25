import sys
sys.stdin = open("input.txt")
'''
1) N과 M이 8보다 클 때
-> 인덱스를 1씩 더해 8*8 사각형을 옮겨 가며 갯수를 구해준다.
2) WB 순서
-> 'W'가 맨 처음 시작할 때 다시 칠해야 되는 갯수
-> 'B'가 맨 처음 시작할 때 다시 칠해야 하는 갯수
'''
# 입력 받기
N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]

# 모든 결과 값을 넣어 둘 temp
temp = []

# N과 M이 8보다 클 시, 큰 숫자만큼 1씩 더해줌
for i in range(N-7):
    for j in range(M-7):
        w_cnt = 0
        b_cnt = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y)%2 == 0:
                    # W가 아니면 W로 칠해주는 갯수를 더함
                    if matrix[x][y] != 'W':
                        w_cnt += 1
                    # B가 아니면 B로 칠해주는 갯수를 더함
                    else:
                        b_cnt += 1
                else:
                    # B가 아니면 B로 칠해주는 갯수를 더함
                    if matrix[x][y] != 'B':
                        w_cnt += 1
                    # W가 아니면 W로 칠해주는 갯수를 더함
                    else:
                        b_cnt += 1

        # 모든 개수를 temp에 append 한다.
        temp.append(w_cnt)
        temp.append(b_cnt)

# 그중 제일 작은 값 출력력
print(min(temp))