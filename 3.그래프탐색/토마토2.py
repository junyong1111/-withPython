import sys
from collections import deque
# sys.stdin = open("input.txt")

steps = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]

M, N, H = map(int, sys.stdin.readline().split())
arr = [[[0]*H for _ in range(M)] for _ in range(N)]
init_flag = False
q = deque()

for h in range(H):
    for i in range(N):
        data = sys.stdin.readline().split()
        for j in range(M):
            arr[i][j][h] = int(data[j])
            if arr[i][j][h] == 0:
                init_flag = True
            elif arr[i][j][h] == 1:
                q.append((j, i, h))

def myprint(arr):
    for h in range(H):
        for i in range(N):
            for j in range(M):
                print(arr[i][j][h], end=' ')
            print()
        print()

def findMaxVal(arr):
    maxVal = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                maxVal = max(maxVal, arr[i][j][h])
    return maxVal
def checktomato():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[i][j][h] == 1:
                    return False
    return True

def checkAnswer():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[i][j][h] == 0:
                    return False
    return True

if init_flag == False:
    print(0)
    sys.exit()
if checktomato() == True:
    print(-1)
    sys.exit()

distance = [[[0]*H for _ in range(M)] for _ in range(N)]

def bfs(q):
    while q:
        x, y, z = q.popleft()
        if distance[y][x][z] == 0:
            distance[y][x][z] = 1
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            nz = z + step[2]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H and arr[ny][nx][nz] == 0 and distance[ny][nx][nz] == 0:
                arr[ny][nx][nz] = 1
                distance[ny][nx][nz] =  distance[y][x][z] +1
                q.append((nx, ny, nz))

bfs(q)


if checkAnswer() == False:
    print(-1)
else:
    ret = findMaxVal(distance)
    print(ret-1)