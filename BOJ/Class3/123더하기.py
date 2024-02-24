import sys
# sys.stdin = open("BOJ/Class3/input.txt")

testcase = int(sys.stdin.readline())
MAX_SIZE = 12

dp = [0] * MAX_SIZE
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, MAX_SIZE):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

while testcase:
    testcase-=1
    n = int(sys.stdin.readline())
    print(dp[n])