'''
크루스칼
1. 그래프의 간선들을 가중치를 기준으로 오름차순 정렬.
2. 정렬된 간선들을 순서대로 선택하되, 간선들이 싸이클을 이루지 않도록
주의하여 탐색한다.
3. 간선의 개수가 n-1개가 될 때까지 반복한다.
'''

import sys
sys.stdin = open("input.txt")

V, E = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(E)]
# 가중치 순으로 정렬
edges.sort(key=lambda x: x[2])
# print(edges)

cnt = 0
total_weight = 0
mst = []

# mst 연결을 위한 data를 dict으로 초기화
data = {key: key for key in range(V + 1)}


def find(node):
    if node != data[node]:
        data[node] = find(data[node])
    return data[node]

def union(a, b):
    root1 = find(a)
    root2 = find(b)
    data[root2] = root1


while len(mst) < V - 1:
    a, b, w = edges.pop(0)

    if find(a) != find(b):
        union(a, b)
        mst.append([a, b])
        total_weight += w

print(total_weight)
