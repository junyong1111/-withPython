import sys
# sys.stdin = open("BOJ/Class3/input.txt")

testcase = int(sys.stdin.readline())
MAX_SIZE = 101

dp = [0] * MAX_SIZE
dp[1] = 1
dp[2] = 1

for i in range(3, MAX_SIZE):
    dp[i] = dp[i-2] + dp[i-3]
    
while testcase:
    testcase-=1
    print(dp[int(sys.stdin.readline())])

    