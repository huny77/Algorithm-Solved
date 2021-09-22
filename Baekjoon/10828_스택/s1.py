import sys
sys.stdin = open("input.txt")

def push(item):
    stack.append(item)

def pop():
    if not stack:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    if len(stack) > 0:
        return 0
    else:
        return 1

def top():
    if len(stack) > 0:
        return stack[-1]
    else:
        return -1

stack = []
N = int(sys.stdin.readline())

for i in range(N):
    item = sys.stdin.readline().split()

    order = item[0]

    if order == "push":
        push(item[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())