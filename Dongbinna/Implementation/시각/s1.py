import sys
sys.stdin = open("input.txt")

'''
하루는 86,400초 (24 * 60 * 60) -> 완전 탐색
'''

# 시간
h = int(input())

cnt = 0

# '시' 증가
for i in range(h + 1):
    # '분' 증가
    for j in range(60):
        # '초' 증가
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있으면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
