import sys
sys.stdin = open("input.txt")

T = int(input())
for _ in range(T):
    stack = []
    ps = list(input())
    for i in ps:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
