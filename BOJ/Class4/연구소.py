import sys
import copy
from itertools import combinations

# sys.stdin = open("BOJ/Class4/input.txt")

MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

virus = []
empty = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            virus.append((j, i))
        elif grid[i][j] == 0:
            empty.append((j, i))
            
def dfs(temp_grid, visit, x, y):
    stack = []
    visit[y][x] = True
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        for move in MOVE:
            nx, ny = x+move[0], y+move[1]
            if 0<=nx<m and 0<=ny<n and temp_grid[ny][nx] == 0 and visit[ny][nx] == False:
                visit[ny][nx] = True
                temp_grid[ny][nx] = 2
                stack.append((nx, ny))

combination = list(combinations(empty, 3))
answer = 0
for combi in combination:
    w1 = combi[0]
    w2 = combi[1]
    w3 = combi[2]
    temp_grid = copy.deepcopy(grid)
    temp_grid[w1[1]][w1[0]] = 1
    temp_grid[w2[1]][w2[0]] = 1
    temp_grid[w3[1]][w3[0]] = 1

    visit = [[False for _ in range(m)] for _ in range(n)]
    for v in virus:
        dfs(temp_grid, visit, v[0], v[1])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_grid[i][j] == 0:
                cnt +=1
    answer = max(answer, cnt)
    
print(answer)