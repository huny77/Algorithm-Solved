import sys
sys.stdin = open("input.txt")

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    ans = (a * b) // gcd(a, b)
    return ans


a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))

