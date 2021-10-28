import sys
sys.stdin = open("input.txt")

N = int(input())
words = []
for _ in range(N):
    words.append(input())
set_words = list(set(words))
set_words.sort()
set_words.sort(key=len)

for i in set_words:
    print(i)