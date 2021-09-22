import sys
sys.stdin = open("input.txt")

word = input()
if word == word[::-1]:
    print("1")
else:
    print("0")