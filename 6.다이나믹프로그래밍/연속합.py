import sys
# sys.stdin = open("6.다이나믹프로그래밍/input.txt")

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n+1)
dp[1] = arr[0]

for i in range(2, n+1):
    dp[i] = max(dp[i-1] + arr[i-1], 0)
if max(dp) == 0:
    print(max(arr))
else :
    print(max(dp))