import sys
sys.stdin = open("9.알고리즘유형별/input.txt")

def myprint(arr, n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(arr[i][j], end=" ")
        print()
        
MAX_SIZE = 5
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
GRID = [['.' for _ in range(MAX_SIZE+1)] for _ in range(MAX_SIZE+1)]
VISIT = [[False for _ in range(MAX_SIZE+1)] for _ in range(MAX_SIZE+1)]
GRID[1][1] = 'A'
VISIT[1][1] = True

GRID[MAX_SIZE][MAX_SIZE] = 'B'
VISIT[MAX_SIZE][MAX_SIZE] = True


n = int(sys.stdin.readline())
for _ in range(n):
    y, x = map(int, sys.stdin.readline().split())
    GRID[y][x] = 'X'
    VISIT[y][x] = True



def checkGrid(nx, ny):
    if GRID[ny][nx] == "." and VISIT[ny][nx] == False:
        return True
    return False

def checkMove(nx, ny):
    if nx <= 0 or nx >MAX_SIZE:
        return False
    if ny <= 0 or ny < MAX_SIZE:
        return False
    return (checkGrid(nx, ny) and True)

def dfs(ax, ay, bx, by):
    if ax == bx and ay == by:
        return 1
    
    paths = 0
    VISIT[ay][ax] = VISIT[by][bx] = True
    
    for move in moves:
        nax, nay = ax + move[0], ay + move[1]
        nbx, nby = bx - move[0], by - move[1]
        if checkMove(nax, nay) and checkMove(nbx, nby):
            
            paths += dfs(nax, nay, nbx, nby)
    VISIT[ay][ax] = VISIT[by][bx] = False
    return paths


        
print(dfs(1, 1, MAX_SIZE, MAX_SIZE))
    

    
# myprint(GRID, MAX_SIZE, MAX_SIZE)
