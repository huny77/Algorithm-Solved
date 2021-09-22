import sys
sys.stdin = open("input.txt")

def dfs(v):
    visited[v] = 1
    for w in range(1, V+1):
        if graph[v][w] == 1 and visited[w] == 0:
            dfs(w)

V = int(input())
E = int(input())
graph = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)
for _ in range(E):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1
dfs(1)
print(visited.count(1)-1)