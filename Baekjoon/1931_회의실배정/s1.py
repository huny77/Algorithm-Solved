import sys
sys.stdin = open("input.txt")

N = int(input())

time = [[0]*2 for _ in range(N+1)]
for i in range(1, N+1):
    s, e = map(int, input().split())
    time[i][0] = s
    time[i][1] = e

# 빨리 끝나는 순으로 정렬
time.sort(key = lambda x: (x[1], x[0]))

# 카운트, 끝나는 시간을 0으로 초기화
cnt = 0
end_time = 0
# N+1까지 반복하면서 시작시간이 끝나는 시간보다 크면 cnt를 1더해주고,
# 끝나는 시간을 end_time으로 바꿔줌
# 그래야 다시 반복하면서 시작 시간이랑 끝나는 시간이랑 겹치는 지 확인 가능
for i in range(1, N+1):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]
print(cnt)