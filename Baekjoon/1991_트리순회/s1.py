# 1. 전위 순회
def pre_order(node):
    if node == ".":
        return

    print(node, end="")
    pre_order(tree[node][0])
    pre_order(tree[node][1])

# 2. 중위 순회
def in_order(node):
    if node == ".":
        return

    in_order(tree[node][0])
    print(node, end="")
    in_order(tree[node][1])

# 3. 후위 순회
def post_order(node):
    if node == ".":
        return

    post_order(tree[node][0])
    post_order(tree[node][1])
    print(node, end="")


# 입력
n = int(input())
# tree dic으로 초기화
tree = {}
# tree 만들기
for i in range(n):
    node, left, right = map(str, input().split())
    tree[node] = [left, right]

# 출력
pre_order("A")
print()
in_order("A")
print()
post_order("A")