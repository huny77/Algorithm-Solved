import sys
sys.stdin = open("input.txt")

n = int(input())
# 바로 list로 받아야 시간 초과가 안나는 듯
students = [list(input().split()) for _ in range(n)]

# 2번째 인덱스는 감소
# 3번째 인덱스는 증가
# 4번째 인덱스는 감소
# 모두 같으면 1번째 인덱스는 증가하는 순으로
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 출력은 이름만
for student in students:
    print(student[0])
