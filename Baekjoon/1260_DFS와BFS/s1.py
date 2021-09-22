import sys
sys.stdin = open("input.txt")

def dfs(V):
    print(V, end=' ')
    visited[V] = 1
    for i in range(1, N+1):
        if visited[i] == 0 and arr[V][i] == 1:
            dfs(i)

def bfs(V):
    Q = []
    Q.append(V)
    visited[V] = 1

    while Q:
        V = Q.pop(0)
        print(V, end=' ')
        for w in range(1, N+1):
            if arr[V][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = 1



N, M, V = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    s, e = list(map(int, input().split()))
    arr[s][e] = 1
    arr[e][s] = 1

dfs(V)
print()
visited = [0] * (N+1)
bfs(V)