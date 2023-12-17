import sys
# sys.stdin = open("input.txt")
MAX_SIZE = 101
testcase = int(sys.stdin.readline())

while testcase:
    testcase-=1
    n = int(sys.stdin.readline())
    
    dp = [0] * MAX_SIZE
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])