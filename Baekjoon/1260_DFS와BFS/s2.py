import sys
sys.stdin = open("input.txt")

from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)