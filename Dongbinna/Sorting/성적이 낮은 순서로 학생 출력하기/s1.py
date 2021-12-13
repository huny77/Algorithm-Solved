import sys
sys.stdin = open("input.txt", 'r', encoding="UTF-8")

n = int(input())

arr = []
for i in range(n):
    student, record = input().split()
    # 이름은 문자열, 성적은 정수형으로 변환하여 저장
    arr.append((student, int(record)))

# 키(key)를 이용하여, 점수를 기준으로 정렬
result = sorted(arr, key=lambda  x: x[1])

for i in range(n):
    print(result[i][0], end=" ")