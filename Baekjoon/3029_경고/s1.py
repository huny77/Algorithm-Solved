import sys
sys.stdin = open("input.txt")

# map을 활용하여 각자 int로 받기
h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

# 모두 초로 바꿔 주기!
t1 = h1 * 60 * 60 + m1 * 60 + s1
t2 = h2 * 60 * 60 + m2 * 60 + s2

# 만약에 t2가 더 크다면 바로 해결하면 된다
# 아니면 하루를 올려서 계산해 줌
if t2 > t1:
    time = t2 - t1
else:
    time = t2 + 24 * 60 * 60 - t1

# 각각 시간, 분, 초로 출력
h = time // 60 // 60
m = time // 60 % 60
s = time % 60

print("%02d:%02d:%02d" %(h, m, s))


