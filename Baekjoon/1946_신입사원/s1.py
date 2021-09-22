import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(1, T+1):
    # 지원자의 숫자
    N = int(input())
    # 리스트를 초기화
    people = []
    # 서류 1등은 합격자이기 때문에 cnt를 1로 시작한다.
    cnt = 1
    for _ in range(1, N+1):
        # first : 서류전형, second : 면접전형
        # 시간 초과때문에 sys.stdin.readline()를 이용한다.
        first, second = map(int, sys.stdin.readline().split())
        people.append([first, second])

    # 서류전형을 기준으로 정렬
    people.sort()
    # 어차피 서류전형 기준으로 정렬했기 때문에 면접으로 비교해야함
    max_val = people[0][1]

    for i in range(1, N):
        if max_val > people[i][1]:
            cnt += 1
            max_val = people[i][1]

    print(cnt)
