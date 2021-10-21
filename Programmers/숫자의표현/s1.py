def solution(n):
    # 숫자의 개수를 셀 cnt 초기화
    cnt = 0
    # 완전탐색 기반
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            # 만약 더한게 n이면 cnt를 올리고
            if temp == n:
                cnt += 1
                break
            # n보다 크면 다시 처음으로 시작한다.
            elif temp > n:
                break
    return cnt