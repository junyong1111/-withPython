import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))
    
prefix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        #-- UP + LEFT + SELF - DUPLICATE(LEFT+UP)
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] + grid[i-1][j-1] - prefix[i-1][j-1]
        
for _ in range(M):
    sy, sx, ey, ex = map(int, input().split())
    #-- 현재 2차원 구간합 => (LEFT + UP - LEFT+UP)
    print(prefix[ey][ex] - (prefix[ey][sx-1] + prefix[sy-1][ex] - prefix[sy-1][sx-1]))