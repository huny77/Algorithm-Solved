import sys
sys.stdin = open("input.txt")

K = int(input())
stack = []
ans = 0
for i in range(K):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
for i in stack:
    ans += i
print(ans)

