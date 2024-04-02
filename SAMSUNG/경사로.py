import sys
from collections import deque

# sys.stdin = open("SAMSUNG/input.txt")

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
        
def ispossible(x, y, target, dir, visit):
    if dir == "up":
        #-- 현재 위치부터 L만큼 내려가면서 공간이 있는지 + 같은 높이인지 확인
        #-- N이 6이라면 현재 위치 + L 5면 가능
        if y+(L-1) >= N :
            return False
        for i in range(y, y+L):
            if target != grid[i][x] or visit[i][x] == True:
                return False
        return True

    elif dir == "down":
        if y-(L-1) < 0:
            return False
        for i in range(y- (L-1), y+1):
            if target != grid[i][x] or visit[i][x] == True:
                return False
        return True

    elif dir == "left":
        if x+(L-1) >= N:
            return False
        for i in range(x, x+L):
            if target != grid[y][i] or visit[y][i] == True:
                return False
        return True
    
    elif dir == "right":
        if x-(L-1) < 0:
            return False
        for i in range(x- (L-1), x+1):
            if target != grid[y][i] or visit[y][i] == True:
                return False
        return True
        
            
            
            
    
def fromUptoDown(x, y, visit):
    curr = grid[y][x] 
    #-- x는 그대로 y만 증가
    idx = 1
    while idx < N:      
        if curr+2 <= grid[idx][x]:
            return False
        #-- 현재 위치랑 -1 차이가 나는 곳이라면 가능성 존재 탐색 시작
        if curr-1 == grid[idx][x]:
            #-- 1. L만큼의 길이가 확보되었는지 확인
            #-- 2. 모두 같은 높이 인지 확인
            if ispossible(x, idx, grid[idx][x], "up", visit) == False:
                return False
            for ny in range(L):
                visit[ny+idx][x] = True
            
            curr = grid[idx][x]
            idx += L
            continue
        elif curr+1 == grid[idx][x]:
            if ispossible(x, idx-1, grid[idx-1][x], "down", visit) == False:
                return False
            for ny in range(L):
                visit[(idx-1)-ny][x] = True
            curr = grid[idx][x]      
            
        #-- 만약 현재 높이랑 같다면 그냥 넘어감
        idx+=1
    return True
        

        
def fromDowntoUp(x, y, visit):
    curr = grid[y][x] 
    #-- x는 그대로 y만 감소
    idx = N-2
    while idx >= 0:
        if curr+2 <= grid[idx][x]:
            return False
        #-- 현재 위치랑 -1 차이가 나는 곳이라면 가능성 존재 탐색 시작
        if curr-1 == grid[idx][x]:
            #-- 1. L만큼의 길이가 확보되었는지 확인
            #-- 2. 모두 같은 높이 인지 확인
            
            if ispossible(x, idx, grid[idx][x], "down", visit) == False:
                return False
            for ny in range(L):
                visit[ny+idx][x] = True
            curr = grid[idx][x]
            idx -= L
            continue
        elif curr+1 == grid[idx][x]:
            if ispossible(x, idx+1, grid[idx+1][x], "up", visit) == False:
                return False
            for ny in range(L):
                visit[(idx+1)-ny][x] = True
            curr = grid[idx][x]
        #-- 만약 현재 높이랑 같다면 그냥 넘어감
        idx-=1
    return True
                
def fromLefttoRight(x, y, visit):
    curr = grid[y][x] 
    #-- y는 그대로 x만 증가
    idx = 1
    while idx < N:
        #-- 현재 위치랑 -1 차이가 나는 곳이라면 가능성 존재 탐색 시작
        if curr+2 <= grid[y][idx]:
            return False
        if curr-1 == grid[y][idx]:
            #-- 1. L만큼의 길이가 확보되었는지 확인
            #-- 2. 모두 같은 높이 인지 확인
            if ispossible(idx, y, grid[y][idx], "left", visit) == False:
                return False
            for nx in range(L):
                visit[y][idx+nx] = True
            curr = grid[y][idx]
            idx += L
            continue
        #-- 올라가는거면 반대에서 내려가는거랑 똑같다!
        elif curr+1 == grid[y][idx]:
            if ispossible(idx-1, y, grid[y][idx-1], "right", visit) == False:
                return False
            for nx in range(L):
                visit[y][(idx-1)+nx] = True
            curr = grid[y][idx]            
        #-- 만약 현재 높이랑 같다면 그냥 넘어감
        idx+=1
    return True   

def fromRighttoLeft(x, y, visit):
    curr = grid[y][x] 
    #-- y는 그대로 x만 증가
    idx = N-2
    while idx >= 0:
        #-- 현재 위치랑 -1 차이가 나는 곳이라면 가능성 존재 탐색 시작
        if curr+2 <= grid[y][idx]:
            return False
            
        if curr-1 == grid[y][idx]:
            #-- 1. L만큼의 길이가 확보되었는지 확인
            #-- 2. 모두 같은 높이 인지 확인
            if ispossible(idx, y, grid[y][idx], "right", visit) == False:
                return False
            for nx in range(L):
                visit[y][nx+idx] = True 
            curr = grid[y][idx]
            idx -= L
            continue
        elif curr+1 == grid[y][idx]:
            if ispossible(idx+1, y, grid[y][idx+1], "left", visit) == False:
                return False
            for nx in range(L):
                visit[y][(idx+1) - nx] = True
            curr = grid[y][idx]       
        #-- 만약 현재 높이랑 같다면 그냥 넘어감
        idx-=1
    return True          
            
answer = 0
while queue:
    x, y, dir = queue.popleft()
    visit = [[False for _ in range(N)] for _ in range(N)]
    
    
    if dir == "up":
        if fromUptoDown(x, y, visit) == True:
            # print("UP!!")
            answer +=1
    elif dir == "down":
        if fromDowntoUp(x, y, visit) == True:
            # print("DOWN!!!")
            answer+=1
    elif dir == "left":
        if fromLefttoRight(x, y, visit)== True:
            # print("LEFT!!!")
            answer +=1
    elif dir == "right":
        if fromRighttoLeft(x, y, visit) == True:
            # print("RIGHT!!!")
            answer +=1
print(answer)

            

#-- 재시도 ㅎ애ㅑ함
