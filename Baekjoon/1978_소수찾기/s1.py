import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))

def Prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

ans = []
for i in range(len(arr)):
    if Prime(arr[i]):
        ans.append(arr[i])
print(len(ans))