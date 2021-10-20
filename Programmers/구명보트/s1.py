"""
구명보드에 2명을 태워야하는데, 최소한으로 구명보트를 이용하기 위해 가장 몸무게가
많이 나가는 사람과 가장 적게 나가는 사람을 계속해서 매칭시켜서 최대한 한 번에 보낸다.

정렬하고, start와 end의 위치 값의 합이 limit를 넘지 않으면 한번에 보낸다.
만약 넘게 된다면 작은 사람은 다른 사람과 태워서 보내면 limit를 넘지 않을 수도 있기
때문에 무거운 사람을 하나 태워서 보낸다.
"""

def solution(people, limit):
    answer = 0
    # 일단 정렬을 시킨다.
    people.sort()
    # 시작과 끝을 정의한다. 0부터 하니까 끝은 당연히 (사람 수-1)
    start = 0
    end = len(people) - 1
    # 투포인터처럼 시작과 끝이 같아질 때까지 탐색
    while start <= end:
        # 일단 한 번 왔다갔다 했다는 것을 증가시키고
        answer += 1
        # 만약 가장 가벼운 사람과 가장 무거운 사람을 더한 것이 무게 제한보다 작으면
        if people[start] + people[end] <= limit:
            # 시작점을 더해주고
            start += 1
        # 끝점을 빼준다.
        end -= 1

    return answer