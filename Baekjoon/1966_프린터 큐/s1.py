import sys
sys.stdin = open("input.txt")

from collections import deque

for _ in range(int(input())):
    # n = 문서의 개수, m = 중요도 개수
    n, m = list(map(int, input().split()))
    # queue는 중요도
    queue = deque(map(int, input().split()))
    temp = deque(range(len(queue)))
    temp[m] = 'target'

    # 순서
    cnt = 0

    while True:
        # 가장 앞에 있는 문서의 중요도 확인
        if queue[0] == max(queue):
            cnt += 1

            # 가장 앞에 있는 문서의 중요도가 가장 높고 찾으려는 target 일 때
            if temp[0] == 'target':
                print(cnt)
                break

            else:
                queue.popleft()
                temp.popleft()

        else:
            queue.append(queue.popleft())
            temp.append(temp.popleft())