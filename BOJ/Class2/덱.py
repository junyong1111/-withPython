import sys
from collections import deque
# sys.stdin = open("input.txt")

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] =="push_back":
        queue.append(int(order[1]))
    elif order[0] == "push_front":
        queue.appendleft(int(order[1]))
    elif order[0] == "pop_back":
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif order[0] == "pop_front":
        if len(queue) != 0:    
            print(queue.popleft())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
