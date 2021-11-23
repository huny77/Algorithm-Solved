import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    arr = list(map(int, input()))
    ans = 0
    for i in range(len(arr)):
        # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우,
        # 곱하기보다는 더하기를 수행
        if ans <= 1 or arr[i] <= 1:
            ans += arr[i]
        else:
            ans *= arr[i]
    print(ans)