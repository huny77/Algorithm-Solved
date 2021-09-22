# import sys
import heapq
# sys.stdin = open("input.txt")

def prim_heapq(node):
    heap = []
    ans = 0
    visited = [0] * (V+1)
    visited[0] = 1

    for temp in arr[node]:
        heapq.heappush(heap, temp)

    while heap:
        w, node = heapq.heappop(heap)
        if not visited[node]:
            ans += w
            visited[node] = 1

            for w, weight in arr[node]:
                if not visited[w]:
                    heapq.heappush(heap, (w, weight))

    return ans

V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for i in range(E):
    s, e, w = map(int, input().split())
    arr[s].append((w, e))
    arr[e].append((w, s))
# edges = [list(map(int, input().split())) for _ in range(V)]
# arr = {key: [] for key in range(V + 1)}
# for s, e, weight in edges:
#     arr[s].append((weight, e))
#     arr[e].append((weight, s))

print(prim_heapq(1))