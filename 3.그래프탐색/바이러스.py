import sys
from collections import deque
sys.setrecursionlimit(101)
# sys.stdin = open('3.그래프탐색/input.txt')

computers = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

graph = [[] for _ in range(computers+1)]

for i in range(edge):
    fromComputer, toComputer = map(int, sys.stdin.readline().split())
    graph[fromComputer].append(toComputer)
    graph[toComputer].append(fromComputer)

visit = [0] * (computers + 1)
queue = deque()

visit[1] = 1
queue.append(1)

def bfs():
    while queue:
        data = queue.popleft()
        for node in graph[data]:
            if (visit[node] == 0):
                visit[node] = 1
                queue.append(node)
bfs()
cnt = -1 #-- 자기 자신은 제외
for i in range(1, computers+1):
    if visit[i] == 1:
        cnt = cnt+1
print(cnt)