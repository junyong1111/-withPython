import sys
sys.setrecursionlimit(100001)
# sys.stdin = open("BOJ/input.txt")

N, K = map(int, sys.stdin.readline().split())
INF = int(1e9)
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))
    
dp = [INF] * (100001)

for coin in coins:
    dp[coin] = 1

def dynamic(n):
    if (dp[n] != INF):
        return dp[n]
    else:
        for coin in coins:
            if(n-coin)<=0:
                dp[n] = min(INF, dp[n])
            else:
                dp[n] = min(dynamic(n-coin), dp[n])
        dp[n]+=1
        return dp[n]

dynamic(K)
if(dp[K] >= INF):
    print(-1)
else:
    print(dp[K])