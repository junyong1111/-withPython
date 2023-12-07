import sys
sys.stdin = open("6.다이나믹프로그래밍/input.txt")

N,M = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coin = int(sys.stdin.readline())
    coins.append(coin)
coins.sort()  
import math

dp = [math.inf] * (max(max(coins), M) +1)
dp[0] = 0
for coin in coins:
    dp[coin] = 1
    


def dynamic_programming(n):
    if(n<0):
        return math.inf
    if dp[n] != math.inf:
        return dp[n]
    else:
        if (n-coins[0]) >=0:
            
            min_value = math.inf
            for coin in coins:
                temp = dynamic_programming(n-coin)
                print(n, coin, temp)
                min_value = min(min_value, temp)
            dp[n] = min_value+1 
            return dp[n]
        else :
            return math.inf
    
dynamic_programming(M)
answer = dp[M]
print(dp)
if answer != math.inf:
    print(answer)
else:
    print(-1)
        