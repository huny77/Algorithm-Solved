def solution(N, stages):
    cnt_pass = [0] * (N + 2)
    cnt_stay = [0] * (N + 2)

    for s in stages:
        cnt_stay[s] += 1
        for i in range(1, N + 1):
            if s >= i:
                cnt_pass[i] += 1

    fail = {}
    answer = []
    for i in range(1, N + 1):
        if cnt_pass[i] == 0:
            fail[i] = 0
        else:
            fail[i] = float(cnt_stay[i] / cnt_pass[i])

    s_fail = sorted(fail.items(), key=lambda x: x[1], reverse=True)

    for n in s_fail:
        answer.append(n[0])
    return answer