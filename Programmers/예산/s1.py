def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if budget <= 0:
            break
        if budget >= d[i]:
            budget = budget - d[i]
            answer += 1
    return answer