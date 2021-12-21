import sys
sys.stdin = open("input.txt")

from collections import deque

n = int(input())
m = int(input())
# dict으로 초기화하고 넣어준다.
graph = { key: [] for key in range(1, n+1) }
visited = [False] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    # 양방향
    graph[s].append(e)
    graph[e].append(s)

def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # 친구 사이라는 뜻
                visited[i] = visited[v] + 1
    return visited

cnt = 0
res = bfs(1)
# [1:]을 하는 이유 : 1부터 시작했기 때문
for i in res[1:]:
    # 자신의 친구와 친구의 친구
    if 1 < i <= 3:
        cnt += 1
print(cnt)
