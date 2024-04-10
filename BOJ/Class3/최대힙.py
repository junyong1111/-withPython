import sys
import heapq

# sys.stdin = open("input.txt")
input = sys.stdin.readline

queue = []
N = int(input())

for _ in range(N):
    order = int(input())

    if order == 0:
        if len(queue) == 0:
            print(0)
        else:
            print(heapq.heappop(queue) * -1)

    else:
        heapq.heappush(queue, (order * -1))
