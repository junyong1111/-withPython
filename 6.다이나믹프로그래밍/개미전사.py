import sys
sys.stdin = open("6.다이나믹프로그래밍/input.txt")

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0] * 101

# dp[n] = arr[n-1]
# dp[n] = arr[n-1]

def dynamic(n):
    if n == 1:
        return arr[n-1]
    if n < 1:
        return 0
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = max(dynamic(n-1), (dynamic(n-2) + arr[n-1]))
        return dp[n]

dynamic(n)        
print(dp[n])