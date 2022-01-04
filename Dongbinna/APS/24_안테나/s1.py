import sys
sys.stdin = open("input.txt")

"""
1. 홀수일 때, 중간 값이 유일한 답
2. 짝수일 때, 중간 값이 2개이므로 위치 상 왼쪽이 더 작음
"""
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

# 미리 -1을 해주는 이유는 뒤에 해주면 홀수일 때를 따로 분리해서 계산해야함 
# 미리 빼줘서 다 짝수로 취급
mid = (n-1) // 2
print(arr[mid])
