import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
stack = []
visited = [False] * (N + 1)

def dfs(depth):
    # 수열의 길이가 M이라면 출력
    # depth = len(stack)
    if depth == M:
        print(*stack)
        return

    # 아니라면,
    for i in range(1, N + 1):
        if visited[i]: continue

        visited[i] = True
        stack.append(i)
        dfs(depth + 1)
        stack.pop()
        visited[i] = False

dfs(0)