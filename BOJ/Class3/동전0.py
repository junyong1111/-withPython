import sys
# sys.stdin = open("BOJ/Class3/input.txt")

N, K = map(int, sys.stdin.readline().split())

coins = []
for i in range(N):
    coins.append(int(sys.stdin.readline()))

#-- 그리디
answer = 0
for coin in reversed(coins):
    if coin <= K:
        answer += K//coin
        K = K%coin
print(answer)
    