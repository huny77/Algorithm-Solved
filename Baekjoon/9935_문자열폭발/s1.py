import sys
sys.stdin = open("input.txt")

# 전체 문자열 입력
string = input()
# 폭발 문자열 입력
bomb = input()

# 스택
stack = []

# 전체 문자열 입력을 돌면서 일단 스택에 넣어준다.
for i in string:
    stack.append(i)
    
    # 스택의 끝 자리와 폭발 문자열의 끝이 같고, 스택의 길이가 문자열 길이보다 같거나 크면
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        # 뒤부터 폭발 문자열이랑 맞는지 대조한다.
        if "".join(stack[-len(bomb):]) == bomb:
            # 그리고 폭발 문자열을 pop 해준다.
            for j in range(len(bomb)):
                stack.pop()

# 스택 안에 뭐가 있으면 해당 문자열 출력
if stack:
    print("".join(stack))
# 없으면 FRULA를 출력
else:
    print("FRULA")

