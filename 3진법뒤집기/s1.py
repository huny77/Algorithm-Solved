def solution(n):
    temp = ''
    while True:
        if n == 0:
            break
        temp += str(n % 3)
        n = n // 3
    answer = int(temp, 3)
    return answer