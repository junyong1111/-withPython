import sys
# sys.stdin = open("BOJ/Class4/input.txt")
MAX_SIZE = 1001
INF = int(1e9)

N = int(sys.stdin.readline())
dp = [[INF for _ in range(MAX_SIZE)] for _ in range(3)]
houses = []
for i in range(N):
    R, G, B = map(int, sys.stdin.readline().split())
    houses.append((R, G, B))
    
# #-- init
dp[0][1] = houses[0][0]  #-- Red
dp[1][1] = houses[0][1] #-- Green
dp[2][1] = houses[0][2] #-- Blue

for i in range(2, N+1):
    dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + houses[i-1][0]
    dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + houses[i-1][1]
    dp[2][i] = min(dp[0][i-1], dp[1][i-1]) + houses[i-1][2]
    
print(min(dp[0][N], dp[1][N], dp[2][N]))