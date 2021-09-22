import sys
sys.stdin = open("input.txt")

def push(item):
    queue.append(item)

def pop():
    if not queue:
        return -1
    else:
        return queue.pop(0)

def size():
    return len(queue)

def empty():
    if len(queue) > 0:
        return 0
    else:
        return 1

def front():
    if len(queue) > 0:
        return queue[0]
    else:
        return -1

def back():
    if len(queue) > 0:
        return queue[-1]
    else:
        return -1

queue = []
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
    elif order == "back":
        print(back())
    elif order == "front":
        print(front())