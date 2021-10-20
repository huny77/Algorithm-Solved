import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
# 숫자 사용 여부를 아는 방문 체크
visited = [False] * (N+1)
# 정답 배열
answer = [0] * M

def dfs(index, N, M):
    # 인덱스가 있어야 해당 순열을 구할 수 있음
    # 없으면 전체 순열
    # index가 M과 같으면 해당 문제를 다 구했기 때문에 출력
    if index == M:
        print(*answer)
        return

    # M에 도달하지 못했다면 다시 찾기
    for i in range(1, N+1):
        # 이미 해당 숫자가 사용되었으면 pass
        if visited[i]:
            continue
        # 해당 숫자가 사용되지 않았다면 True로 바꾸고 정답 배열을 기록해준다.
        visited[i] = True
        answer[index] = i
        # 재귀 호출
        dfs(index+1, N, M)
        # 재귀가 끝나면 다시 되돌아 갈 때 사용하지 않았던 상태로 되돌려주기
        visited[i] = False

dfs(0, N, M)