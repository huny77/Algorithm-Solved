import sys
sys.stdin = open('input.txt')


def binary_search(left, right, target):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0


n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
arr2 = list(map(int, input().split()))

for target in arr2:
    print(binary_search(0, len(arr) - 1, target))