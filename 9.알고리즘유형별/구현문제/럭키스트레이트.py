import sys
import math
sys.stdin = open("9.알고리즘유형별/input.txt")
n = int(sys.stdin.readline())

def luckyStrike(n):
    lucky = str(n)
    data = list(map(int, lucky))
    left = 0
    right = 0
    for i in range(len(lucky)//2):
        left += data[i]
    for i in range(len(lucky)//2, len(lucky)):
        right += data[i]
    return left == right
    
if luckyStrike(n):
    print("LUCKY")
else:
    print("READY")    