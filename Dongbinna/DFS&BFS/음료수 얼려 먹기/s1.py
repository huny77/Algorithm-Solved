import sys
sys.stdin = open("input.txt")

"""
1. 특정 지점 주변의 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문합니다.
2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있습니다.
3. 모든 노드에 대하여 1 ~ 2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트합니다.
"""

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# DFS로 특정 노드를 방문하고 연결된 모든 모드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if -1 >= x or x >= n or -1 >= y or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드를 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
print(result)