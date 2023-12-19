import sys
sys.stdin = open("6.다이나믹프로그래밍/input.txt")
MAX_SIZE = 10001
n = int(sys.stdin.readline())
wine = []
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

dp = [[0 for _ in range(MAX_SIZE)] for _ in range(4)]
dp[0][1] = wine[0]
dp[1][1] = wine[0]
dp[2][1] = 0
dp[3][1] = wine[0]

maxValue = wine[0]
for i in range(2, n+1):
    curr_wine = wine[i-1]
    dp[3][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
    #case1 : 연속으로 마시는 경우 이전에서 1잔 + 자기 자신
    dp[0][i] = max(dp[1][i-1], dp[3][i]) + curr_wine
    #case2 : 1잔만 마시는 경우 이전에서 0잔  + 자기자신
    dp[1][i] = max(dp[2][i-1], dp[3][i]) + curr_wine
    #case3 : 0잔만 마시는 경우 이전에서 
    dp[2][i] = max(dp[0][i-1], dp[1][i-1], dp[3][i])
    
    maxValue = max(maxValue, dp[0][i], dp[1][i], dp[2][i], dp[3][i])
print(maxValue)    

for i in range(4):
    for j in range(1, n+1):
        print(dp[i][j], end=' ')
    print()
