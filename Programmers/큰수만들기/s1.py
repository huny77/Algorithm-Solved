"""
이 문제는 stack을 활용해서 풀어야 시간초과 되지 않는다.
"""

def solution(number, k):
    stack = []
    for num in number:
        # 스택이 비어있거나 스택의 마지막 숫자보다 숫자가 크거나 k가 0보다 크면
        while stack and stack[-1] < num and k > 0:
            # 스택에서 빼고 k를 -1한다.
            stack.pop()
            k -= 1
        # 그리고 스택에 넣음
        stack.append(num)

    # 답을 적을 때, k가 0이 아닌 경우, 스택 뒤의 k범위까지 슬라이싱
    if k != 0:
        stack = stack[:-k]
    return "".join(stack)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))