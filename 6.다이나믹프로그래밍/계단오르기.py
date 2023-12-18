# https://jypark1111.tistory.com/195
import sys
# sys.stdin = open("6.다이나믹프로그래밍/input.txt")

n = int(sys.stdin.readline())
dp = [[0 for _ in range(n+1)] for _ in range(3)]

stair = []
for _ in range(n):
    stair.append(int(sys.stdin.readline()))

dp[0][1] = stair[0] #-- 연속 
dp[1][1] = stair[0] #-- 밝 
dp[2][1] = 0 #-- 안밟

if n<=1:
    print(max(stair))
else:
    for i in range(2, n+1):
        #-- 연속 밟은경우 1칸 밟은 경우 + 자기 자신
        dp[0][i] =  dp[1][i-1] + stair[i-1]
        #-- 처음 밟은 경우 0번 밟은 경우 + 자기 자신
        dp[1][i] = dp[2][i-1] + stair[i-1]
        #-- 안 밝은 경우 밟은 경우 중 최댓값
        dp[2][i] = max(dp[0][i-1], dp[1][i-1])
    
    print(max(dp[0][n], dp[1][n])) #-- 마지막은 밟아야 하므로 안 밟은 경우는 제외
    