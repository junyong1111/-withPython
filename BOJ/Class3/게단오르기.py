import sys
# sys.stdin = open("BOJ/Class3/input.txt")

MAX_SIZE = 301

N = int(sys.stdin.readline())
stairs = []
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

dp = [[0 for _ in range(MAX_SIZE)] for _ in range(3)]
dp[0][1] = stairs[0] #-- 연속으로 밟는 경우
dp[1][1] = stairs[0] #-- 1개만 밟는 경우
dp[2][1] = 0 #-- 안밟는 경우

    
for i in range(2, N+1):
    dp[0][i] = dp[1][i-1] + stairs[i-1] #-- 이전 1개만 밟고 해당 계단 밟기
    dp[1][i] = dp[2][i-1] + stairs[i-1] #-- 자기 자신만 밟기
    dp[2][i] = max(dp[0][i-1], dp[1][i-1])
    
print(max(dp[0][N], dp[1][N]))
