"""
stack으로 푸는 문제. memory 관리 때문
접근하기가 살짝 어려웠음
"""
def solution(s):
    stack = []

    # 문자열 만큼 반복하면서
    for i in range(len(s)):
        # 스택이 비어있으면 추가
        if not stack:
            stack.append(s[i])
        # 스택이 차있을 경우
        else:
            # 비교하려는 문자열과 스택의 마지막으로 들어간 수를 비교해서 같으면 pop
            if s[i] == stack[-1]:
                stack.pop()
            # 다르면 다시 추가하여 다음 문자와 비교
            else:
                stack.append(s[i])

    if not stack:
        return 1
    else:
        return 0

s = "baabaa"
print(solution(s))