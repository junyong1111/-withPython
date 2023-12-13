import sys
from collections import deque
sys.setrecursionlimit(30000)
sys.stdin = open("3.그래프탐색/input.txt")

testcase = int(sys.stdin.readline())

while testcase:
    testcase-= 1
    
    node, edge = map(int, sys.stdin.readline().split())
    colors = [0] * (node+1)
    # [0, 1, 2, 3]
    # [X, 0, 0, 0]
    graph = [[] for _ in range(node+1)]
    
    for _ in range(edge):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    
    
    def bfs(node, color):
        q = deque()
        q.append(node)
        colors[node] = color
        flag = True
        while q:
            if flag == False:
                return -1
            n = q.popleft()
            for node in graph[n]:
                #== 3나옴
                if colors[node] == 0: #-- 처음 방문
                    if color == 1:
                        color = 2
                        colors[node] = color
                    else:
                        color = 1
                        colors[node] = color
                    q.append(node)
                elif colors[node] == color:
                    flag = False
                    break
                else:
                    continue
        return 0
    curr = 1
    for i in range(1, node+1):
        if colors[i] == 0:
            ans = bfs(i, curr)
    # if ans == 0:
    #     print('YES')
    # else:
    #     print("NO")