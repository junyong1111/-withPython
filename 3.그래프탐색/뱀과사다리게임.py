import sys
from collections import deque
# sys.stdin = open('3.그래프탐색/input.txt')

MAX_SIZE = 101
N, M = map(int, sys.stdin.readline().split())
dice = [1, 2, 3, 4, 5, 6]
board = [0] * MAX_SIZE
distance = [-1] * MAX_SIZE
ladder = dict()
snake = dict()
start = 1
finish = 100

def myprint():
    for i in range(1, MAX_SIZE):
        print(board[i], end= ' ')

for _ in range(N):  #-- 사다리 = -1
    _from, _to = map(int, sys.stdin.readline().split())
    board[_from] = -1
    ladder[_from] = _to
    

for _ in range(M): #-- 뱀 = -2
    _from, _to = map(int, sys.stdin.readline().split())
    board[_from] = -2
    snake[_from] = _to

def bfs(start):
    q = deque()
    distance[start] = 0
    q.append(start)
    flag = False
    while q:
        if flag == True:
            break
        node = q.popleft()
        for d in dice:
            nnode = node + d
            if nnode>=1 and nnode<MAX_SIZE and distance[nnode] == -1:
                if board[nnode] == -1 : #-- 사다리
                    distance[nnode] = distance[node]+1
                    nnode = ladder[nnode] #-- 사다리 탐
                    if distance[nnode] == -1: #-- 처음 탄 사다리라면 갱신
                        distance[nnode] = distance[node]+1
                elif board[nnode] == -2: #-- 뱀
                    distance[nnode] = distance[node]+1
                    nnode = snake[nnode]
                    if distance[nnode] == -1:
                        distance[nnode] = distance[node]+1
                else:
                    distance[nnode] = distance[node]+1
                if nnode == finish:
                    flag = True
                    break
                q.append(nnode)
                    
bfs(start)   
print(distance[finish])       