import sys
sys.stdin = open("BOJ/Class4/input.txt")
MAX_SIZE = 1001

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [0] * (MAX_SIZE)
dp[1] = 1

for i in range(2, N+1):
    if numbers[i-1] > numbers[i-2] :
        dp[i] = dp[i-1] + 1
    elif numbers[i-1] < numbers[i-2]:
        dp[i] = dp[i-2] + 1
    else:
        dp[i] = dp[i-1]
print(dp[N])