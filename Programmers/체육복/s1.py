def solution(n, lost, reserve):
    # 여벌의 체육복이 있는 학생도 도난 당할 수 있기 때문에 set으로 중복 제거
    setLost = set(lost) - set(reserve)
    setReserve = set(reserve) - set(lost)

    for i in setReserve:
        # 왼쪽 학생 먼저
        if i - 1 in setLost:
            setLost.remove(i - 1)
        # 없다면 오른쪽 학생
        elif i + 1 in setLost:
            setLost.remove(i + 1)

    return n - len(setLost)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))