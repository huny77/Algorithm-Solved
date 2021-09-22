import sys
sys.stdin = open("input.txt")


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
print(edges)