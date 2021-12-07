import sys
sys.stdin = open("input.txt")
a, b = map(int, input().split())

# 최대 공약수
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# 최소 공배수
def lcm (a, b):
    return (a * b) // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))