import sys
# sys.stdin = open("input.txt")
N = int(sys.stdin.readline())
MAX_SIZE = 1000000
dp = [0] * (MAX_SIZE+1)

dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[N])