def solution(s, n):
    answer = ''
    s = list(s)
    for i in s:
        if i == ' ':
            answer += ' '
        elif ord(i) >= 97:
            if ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        else:
            if ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)

    return answer