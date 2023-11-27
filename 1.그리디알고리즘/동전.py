import sys
sys.stdin = open("1.그리디알고리즘/input.txt")
n, target = map(int, sys.stdin.readline().split())

coins = [0 for i in range(n)]
for i in range(n):
    coins[i] = int(sys.stdin.readline().rstrip())
coins.reverse()
answer = 0
for coin in coins:
    if coin <= target: #-- 가장 큰 돈으로 거슬러 줄 수 있음
        answer += target // coin 
        target = target % coin
print(answer)