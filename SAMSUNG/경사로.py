import sys
from collections import deque

sys.stdin = open("SAMSUNG/input.txt")

def myprint(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()
    print("== MY DATA ==")

input = sys.stdin.readline
N, L = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

    
# myprint(grid, N, N)

queue = deque()

for i in range(N):
    if grid[0][i] >= grid[N-1][i]:
        queue.append([i, 0, "up"]) #-- x, y
    else:
        queue.append([i, N-1, "down"])

for i in range(N):
    if grid[i][0] >= grid[i][N-1]:
            queue.append([0, i, "left"]) #-- x, y
    else:
        queue.append([N-1, i, "right"])
        
def ispossible(x, y, target, dir):
    if dir == "up":
        #-- 현재 위치부터 L만큼 내려가면서 공간이 있는지 + 같은 높이인지 확인
        #-- N이 6이라면 현재 위치 + L 5면 가능
        if y+(L-1) >= N :
            return False
        for i in range(y, y+L):
            if target != grid[i][x]:
                return False
        return True

    elif dir == "down":
        if y-(L-1) < 0:
            return False
        for i in range(y- (L-1), y+1):
            if target != grid[i][x]:
                return False
        return True

    elif dir == "left":
        if x+(L-1) >= N:
            return False
        for i in range(x, x+L):
            if target != grid[y][i]:
                return False
        return True
    
    elif dir == "right":
        if x-(L-1) < 0:
            return False
        for i in range(x- (L-1), x+1):
            if target != grid[y][i]:
                return False
        return True
        
            
            
            
    
def fromUptoDown(x, y):
    curr = grid[y][x] 
    #-- x는 그대로 y만 증가
    idx = 1
    while idx < N:
        #-- 만약 현재 높이보다 더 크다면 아웃
        if curr < grid[idx][x]:
            return False
        #-- 현재 위치랑 -1 차이가 나는 곳이라면 가능성 존재 탐색 시작
        if curr-1 == grid[idx][x]:
            #-- 1. L만큼의 길이가 확보되었는지 확인
            #-- 2. 모두 같은 높이 인지 확인
            if ispossible(x, idx, grid[idx][x], "up") == False:
                return False
            curr = grid[idx][x]
            idx += L
            continue
        #-- 만약 현재 높이랑 같다면 그냥 넘어감
        idx+=1
    return True
        

        
def fromDowntoUp(x, y):
    curr = grid[y][x] 
    #-- x는 그대로 y만 감소
    idx = N-2
    while idx >= 0:
        #-- 만약 현재 높이보다 더 크다면 아웃
        if curr < grid[idx][x]:
            return False
        #-- 현재 위치랑 -1 차이가 나는 곳이라면 가능성 존재 탐색 시작
        if curr-1 == grid[idx][x]:
            #-- 1. L만큼의 길이가 확보되었는지 확인
            #-- 2. 모두 같은 높이 인지 확인
            if ispossible(x, idx, grid[idx][x], "down") == False:
                return False
            curr = grid[idx][x]
            idx -= L
            continue
        #-- 만약 현재 높이랑 같다면 그냥 넘어감
        idx-=1
    return True
                
def fromLefttoRight(x, y):
    curr = grid[y][x] 
    #-- y는 그대로 x만 증가
    idx = 1
    while idx < N:
        #-- 만약 현재 높이보다 더 크다면 아웃
        if curr < grid[y][idx]:
            return False
        #-- 현재 위치랑 -1 차이가 나는 곳이라면 가능성 존재 탐색 시작
        if curr-1 == grid[y][idx]:
            #-- 1. L만큼의 길이가 확보되었는지 확인
            #-- 2. 모두 같은 높이 인지 확인
            if ispossible(idx, y, grid[y][idx], "left") == False:
                return False
            curr = grid[y][idx]
            idx += L
            continue
        #-- 만약 현재 높이랑 같다면 그냥 넘어감
        idx+=1
    return True   

def fromRighttoLeft(x, y):
    curr = grid[y][x] 
    #-- y는 그대로 x만 증가
    idx = N-2
    while idx >= 0:
        #-- 만약 현재 높이보다 더 크다면 아웃
        if curr < grid[y][idx]:
            return False
        #-- 현재 위치랑 -1 차이가 나는 곳이라면 가능성 존재 탐색 시작
        if curr-1 == grid[y][idx]:
            #-- 1. L만큼의 길이가 확보되었는지 확인
            #-- 2. 모두 같은 높이 인지 확인
            if ispossible(idx, y, grid[y][idx], "right") == False:
                return False
            curr = grid[y][idx]
            idx -= L
            continue
        #-- 만약 현재 높이랑 같다면 그냥 넘어감
        idx-=1
    return True          
            
answer = 0
test = deque()

while queue:
    x, y, dir = queue.popleft()
    
    if dir == "up":
        if fromUptoDown(x, y) == True:
            print("UP!!")
            answer +=1
    elif dir == "down":
        if fromDowntoUp(x, y) == True:
            print("DOWN!!!")
            answer+=1
    elif dir == "left":
        if fromLefttoRight(x, y)== True:
            answer +=1
    elif dir == "right":
        if fromRighttoLeft(x, y) == True:
            answer +=1
print(answer)

            

