import sys, math
sys.stdin = open("input.txt")


def Prime(n):
    n = n+1
    temp = [True] * n
    m = int(math.sqrt(n))
    for i in range(2, m+1):
        if temp[i] == True:
            for j in range(2*i, n, i):
                temp[j] = False

    result = []
    for i in range(2, n):
        if temp[i] == True:
            result.append(i)
    return result


n = int(input())
print(len(Prime(n)))


