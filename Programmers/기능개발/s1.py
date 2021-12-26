def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    # 개발이 다 없어질때까지 반복
    while len(progresses) > 0:
        # 처음 개발부터 속도와 일을 합친 것이 100을 넘으면 둘다 pop하고 카운트 증가
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1

    answer.append(count)

    return answer

# progressess = [93, 30, 55]
progressess = [95, 50, 99, 99, 80, 99]
# speeds = [1, 30, 5]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progressess, speeds))