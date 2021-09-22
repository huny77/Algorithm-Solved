import sys
sys.stdin = open("input.txt")

def bfs(v):
    Q = [v]
    visited[v] = 1
    while Q:
        t = Q.pop(0)
        for w in range(1, V+1):
            if graph[t][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = 1

V = int(input())
E = int(input())
graph = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)

for _ in range(E):
    s, e = map(int, input().split())
    graph[s][e], graph[e][s] = 1, 1
bfs(1)
print(visited.count(1)-1)