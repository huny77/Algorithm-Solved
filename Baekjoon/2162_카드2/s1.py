import sys
sys.stdin = open("input.txt")

# 시간 초과로 인해 deque를 써야 한다.
from collections import deque
N = int(input())
# 카드를 deque로 받고 넣어준다.
cards = deque()
for i in range(1, N+1):
    cards.append(i)

# 카드가 1장 남을 때까지 반복
while True:
    if len(cards) == 1:
        break
    else:
        # 맨 앞에 있는 카드를 뺀다.
        cards.popleft()
        # 맨 앞에 있는 카드를 빼고 맨 뒤에 넣어준다.
        cards.append(cards.popleft())
print(cards[0])
