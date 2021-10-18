import sys
sys.stdin = open('input.txt')

# 입력을 받음
N = int(input())
# 카운트할 숫자, 처음 숫자를 1로 초기화
cnt, num = 1, 1
while True:
    # 1이면 무조건 1
    if N == 1:
        print('1')
        break
    # 아니면 다음 단계로
    else:
        # 육각형이므로 6씩 곱해서 더해줘야함
        num += cnt * 6
        # 만약 한 바퀴를 돌았을 때 N이 해당 범위내에 있으면
        if N <= num:
            # 바로 cnt+1이 정답, 왜냐면 cnt+1이 방을 지나는 횟수
            print(cnt+1)
            break
        # 아니면 다시 cnt 돌면서 N이 해당 범위에 있을 때를 찾음
        else:
            cnt += 1