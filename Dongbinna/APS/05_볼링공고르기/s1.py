import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
temp = [0] * 11

for i in arr:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    temp[i] += 1

ans = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    n -= temp[i]
    # B가 선택하는 경우의 수와 곱하기
    ans += temp[i] * n
print(ans)
