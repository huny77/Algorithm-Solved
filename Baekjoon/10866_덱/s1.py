import sys
sys.stdin = open("input.txt")

def push_back(item):
    deque.append(item)

def push_front(item):
    deque.insert(0, item)

def pop_front():
    if not deque:
        return -1
    else:
        return deque.pop(0)

def pop_back():
    if not deque:
        return -1
    else:
        return deque.pop()

def size():
    return len(deque)

def empty():
    if len(deque) > 0:
        return 0
    else:
        return 1

def front():
    if len(deque) > 0:
        return deque[0]
    else:
        return -1

def back():
    if len(deque) > 0:
        return deque[-1]
    else:
        return -1

deque = []
N = int(sys.stdin.readline())

for i in range(N):
    item = sys.stdin.readline().split()

    order = item[0]

    if order == "push_back":
        push_back(item[1])
    elif order == "push_front":
        push_front(item[1])
    elif order == "pop_back":
        print(pop_back())
    elif order == "pop_front":
        print(pop_front())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "back":
        print(back())
    elif order == "front":
        print(front())