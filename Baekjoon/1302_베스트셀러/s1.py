import sys
sys.stdin = open("input.txt")

n = int(input())

# 개수를 같이 세기 위해 dict으로 넣음
books = {}
for _ in range(n):
    book = sys.stdin.readline().strip()
    # 없으면 1로 넣어주고, 있으면 기존 수에서 +1
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

best_seller = []
for book, cnt in books.items():
    if cnt == max(books.values()):
        best_seller.append(book)

best_seller.sort()
print(best_seller[0])