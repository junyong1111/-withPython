import sys
import heapq

# sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    order = int(input())

    if order == 0:
        try:
            print(heapq.heappop(queue)[1])
        except:
            print(0)
    else:
        heapq.heappush(queue, (abs(order), order))
