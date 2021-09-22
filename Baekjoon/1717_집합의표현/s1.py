"""
유니온 파인드 알고리즘
- '합집합 찾기' 라는 의미
"""
import sys
sys.stdin = open("input.txt")

def find_set(x):
    # x가 루트노드이면 자기 자신 반환
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

# 0.0009958744049072266
# def find_set(x):
#     if p[x] == x:
#         return x
#     p[x] = find_set(p[x])
#     return p[x]

def union(x, y):
    # x와 y의 루트 노드를 찾아준다.
    x, y = find_set(x), find_set(y)
    # x의 부모를 y로 만들어 합쳐주기
    p[find_set(y)] = find_set(x)

N, M = map(int, input().split())
p = [i for i in range(N+1)]

for _ in range(M):
    oper, a, b = map(int, input().split())

    if oper:
        find_A = find_set(a)
        find_B = find_set(b)

        if find_A == find_B:
            print("YES")
        else:
            print("NO")
    # 합집합
    else:
        union(a, b)