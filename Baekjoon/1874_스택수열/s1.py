import sys
sys.stdin = open("input.txt")

n = int(input())
stack = []
ans = []
# 불가능할 경우를 위한 flag
flag = True
current = 0

for _ in range(n):
    x = int(input())
    # 현재 수가 x보다 작을 때까지 반복하면서 append할 땐 +를 답에 기록
    while current < x:
        current += 1
        stack.append(current)
        ans.append("+")
    # 스택의 마지막 수가 입력받은 값과 같으면 pop하면서 -를 답에 기록
    if stack[-1] == x:
        stack.pop()
        ans.append("-")
    # 만약 stack의 마지막 값과 x가 같아지지 않는 경우 flag를 False로 저장
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    print("\n".join(ans))