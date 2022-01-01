import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1
for i in arr:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < i:
        break
    target += i
# 만들 수 없는 금액
print(target)