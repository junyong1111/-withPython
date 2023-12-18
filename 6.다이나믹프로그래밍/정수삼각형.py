import sys
# sys.stdin = open("6.다이나믹프로그래밍/input.txt")

n = int(sys.stdin.readline())
triangle = [[0 for _ in range(n)] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    data = sys.stdin.readline().split()
    for j in range(len(data)):
        triangle[i][j] = int(data[j])
        
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1]+ triangle[i][j], dp[i-1][j]+ triangle[i][j])
            
print(max(dp[n-1]))