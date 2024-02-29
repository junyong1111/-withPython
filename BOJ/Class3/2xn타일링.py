import sys
# sys.stdin = open("BOJ/Class3/input.txt")

MAX_SIZE = 1001
MOD = 10007
dp = [0] * MAX_SIZE

n = int(sys.stdin.readline())

dp[1] = 1
dp[2] = 2

for i in range(3, MAX_SIZE):
    dp[i] = (dp[i-1] + dp[i-2])%MOD

print(dp[n] % MOD)