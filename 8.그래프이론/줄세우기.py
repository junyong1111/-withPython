import sys
from collections import deque
# sys.stdin = open("input.txt")

n, m = map(int, sys.stdin.readline().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    q = deque()
    ret = []
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)
    while q:
        data = q.popleft()
        print(data, end=' ')
        for node in graph[data]:
            if indegree[node] != 0:
                indegree[node] -=1
                if indegree[node] == 0:
                    q.append(node)

topology_sort()