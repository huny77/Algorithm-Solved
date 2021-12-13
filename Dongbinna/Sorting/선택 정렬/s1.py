"""
선택 정렬이란?
- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와
바꾸는 것을 반복합니다.
- 시간 복잡도 : O(N^2)
"""
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i   # 가장 작은 원소의 인덱스
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i] # 스와프

print(arr)