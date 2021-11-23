import sys
sys.stdin = open("input.txt")

# n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 초과할 수 없는 숫자
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

# arr을 큰 수부터 정렬
arr.sort(reverse=True)
first = arr[0]  # 제일 큰 수
second = arr[1] # 두 번째 큰 수

ans = 0

while True:
    # 가장 큰 수를 k번 더하기
    for i in range(k):
        if m == 0: break
        ans += first
        m -= 1
    if m == 0: break
    # 두 번째 큰 수를 1번 더하기
    ans += second
    m -= 1
print(ans)
