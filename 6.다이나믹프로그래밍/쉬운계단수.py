import sys
# sys.stdin = open("6.다이나믹프로그래밍/input.txt")

n = int(sys.stdin.readline())
MOD = 1000000000
dp = [[0 for _ in range(10)] for _ in range(n+1)]

def myprint(arr):
    for i in range(1, n+1):
        for j in range(10):
            print(arr[i][j], end=' ')
        print()

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]%MOD
            continue
        if j == 9:
            dp[i][j] = dp[i-1][j-1]%MOD
            continue
        dp[i][j] = (dp[i-1][j+1] + dp[i-1][j-1])%MOD

print(sum(dp[n])%MOD)
# myprint(dp)