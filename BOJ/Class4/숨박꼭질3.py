import sys
from collections import deque
# sys.stdin = open("BOJ/Class4/input.txt")
input = sys.stdin.readline
MAX_SIZE = 100000

moves = [2, 1, -1]

N, K = map(int, input().split())
if N == K:
    print(0)
    sys.exit()


distacne = [0] * (MAX_SIZE*2)
def bfs(start):
    queue = deque()
    queue.append(start)
    distacne[start] = 1
    
    while queue:
        point = queue.popleft()
        for move in moves:
            if move < 2:
                np = point + move
                if 0 <= np <= MAX_SIZE and distacne[np] == 0:
                    distacne[np] = distacne[point] +1
                    if np == K:
                        return distacne[np]
                    queue.append(np)
            else:
                np = point * move
                if 0 <= np <= MAX_SIZE and distacne[np] == 0:
                    distacne[np] = distacne[point]
                    if np == K:
                        return distacne[np]
                    queue.append(np)
print(bfs(N)-1)