import sys
from collections import deque
# sys.stdin = open('3.그래프탐색/input.txt')

steps = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
testcase = int(sys.stdin.readline())

def myPrint(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
        
while testcase:
    testcase-=1
    
    n = int(sys.stdin.readline())
    board = [[-1 for _ in range(n)] for _ in range(n)]

    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    
    q = deque()
    q.append((sx, sy))
    board[sy][sx] = 0
    
    def bfs(q):
        flag = False
        while q:
            if flag == True:
                break
            x, y = q.popleft()
            for step in steps:
                nx = x + step[0]
                ny = y + step[1]
                if nx >= 0 and ny >= 0 and nx < n and ny < n and board[ny][nx] ==-1:
                    board[ny][nx] = board[y][x]+1
                    if nx == ex and ny == ey:
                        flag = True
                        break
                    q.append((nx, ny))
    bfs(q)
    print(board[ey][ex])