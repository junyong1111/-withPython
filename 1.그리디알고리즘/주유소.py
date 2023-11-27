import sys
# sys.stdin = open('1.그리디알고리즘/input.txt')

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(len(price))]

dp[0] = price[0]
for i in range(1, len(dp)):
    dp[i] = min(dp[i-1], price[i])

answer = 0
for i in range(len(distance)):
    answer += distance[i] * dp[i]
print(answer)