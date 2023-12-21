import sys
sys.stdin = open("9.알고리즘유형별/그리디/input.txt")

n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))

coins = sorted(coins)
flag = False
MAX_SIZE = int(1001)
for i in range(1, MAX_SIZE):
    target = i
    
    for coin in reversed(coins):
        flag = False
        if target-coin < 0:
            continue
        if target-coin > 0:
            target-= coin
        else:
            flag  = True
            break
    if flag == False:
        print(i)
        break
