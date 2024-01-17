import sys
from queue import PriorityQueue
# sys.stdin = open("BOJ/Class3/input.txt")

n = int(sys.stdin.readline())
pq = PriorityQueue()

for _ in range(n):
    order = int(sys.stdin.readline())
    if order == 0 :
        if pq.empty() == False:
            print(pq.get()[1])
        else:
            print(0)
        continue

    if order < 0 :
        priority = order * -1
        pq.put((priority, order))
        continue
    pq.put((order, order))