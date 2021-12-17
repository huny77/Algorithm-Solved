import sys
sys.stdin = open("input.txt")

arr = []
for i in range(5):
    arr.append(input())

ans = ''
# 가로가 최대 15칸
for i in range(15):
    # 세로가 최대 5칸
    for j in range(5):
        # list out of ranges에 안걸리게 하기 위함
        if i >= len(arr[j]):
            continue
        else:
            ans += arr[j][i]
print(ans)