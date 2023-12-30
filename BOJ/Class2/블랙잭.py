import sys
# sys.stdin = open("BOJ/Class2/input.txt")

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards = sorted(cards)


maxValue = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp = cards[i] + cards[j] + cards[k]
            if temp <= m: #-- M보다 작거나 같은 경우만 갱신
                maxValue = max(maxValue, temp)
print(maxValue)