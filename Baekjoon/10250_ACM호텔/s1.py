import sys
sys.stdin = open("input.txt")

T = int(input())
# H: 호텔의 층 수, W: 각 층의 방 수, N: 몇 번째 손님
for _ in range(1, T+1):
    H, W, N = map(int, input().split())
    # 층수는 몇 번째 손님을 높이로 나눈 나머지
    floor = N % H
    # 룸 번호는 몇 번째 손님을 높이로 나눈 몫의 + 1
    room = N // H + 1
    # 예외 : 0이 될 경우는 룸 번호를 빼주고, 높이를 H로 설정
    if floor == 0:
        room -= 1
        floor = H
    print(floor * 100 + room)

