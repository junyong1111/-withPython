import sys
from collections import deque
# sys.stdin = open("BOJ/Class3/input.txt")

MAX_SZ = 100001
N, K = map(int, sys.stdin.readline().split())

moves = [-1, 1, 2]
queue = deque()

distance = [-1] * (MAX_SZ)
queue.append(N)
distance[N] = 0

while queue:
    flag = False
    point = queue.popleft()
    for move in moves:
        if move != 2:
            np = point + move
        else:
            np = move * point
        if 0<= np <  MAX_SZ and distance[np] == -1:
            distance[np] = distance[point]  +1
            queue.append(np)
            if np == K:
                flag = True
                break
    if flag:
        break

print(distance[K])