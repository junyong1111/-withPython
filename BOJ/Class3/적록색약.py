import sys
# sys.stdin = open("BOJ/Class3/input.txt")
input = sys.stdin.readline

N = int(input())
grid = [["" for _ in range(N)] for _ in range(N)]

for i in range(N):
    data = input().split()
    for j in range(N):
        grid[i][j] = data[0][j]

def myprint(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end=" ")
        print()

# myprint(grid, N, N)

#-- init()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(X, Y, visit):
    stack = []
    stack.append([X, Y])
    visit[Y][X] = True
    
    while stack:
        x, y = stack.pop()
        target = grid[y][x] #-- R
        #-- 상하좌우 탐색
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #-- 범위 안에 있으면서 방문하지 않은 같은 색상에 노드
            if 0 <= nx < N and 0 <= ny < N and visit[ny][nx] == False and grid[ny][nx] == target:
                #-- 방문 체크 후 스택에 추가
                visit[ny][nx] = True
                stack.append([nx, ny])
        
        
    

#-- step1. 구역별로 그래프 탐색 시작

visit = [[False for _ in range(N)] for _ in range(N)]
notRedGreen = 0
RedGreen = 0
for i in range(N):
    for j in range(N):
        #-- 방문하지 않았던 곳을 방문하면서 체크
        if visit[i][j] == False:
            dfs(j, i, visit) #-- X, Y, 방문 배열
            notRedGreen +=1
print(notRedGreen, end= " ")

#-- step2. 그리드에 있는 적색을 녹색으로 모두 변경 후 다시 재 탐색
#-- visit 배열 재할당 + 적색을 녹색으로 

for i in range(N):
    for j in range(N):
        visit[i][j] = False
        if grid[i][j] == "R":
            grid[i][j] = "G"

for i in range(N):
    for j in range(N):
        if visit[i][j] == False:
            dfs(j, i, visit)
            RedGreen +=1
            
print(RedGreen)