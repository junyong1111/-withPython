import sys
import bisect
from bisect import bisect_left, bisect_right
# sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

# 4 1 5 2 3
# 1 3 7 9 5
arr = sorted(arr)

for target in targets:
    left = bisect_left(arr, target) 
    right = bisect_right(arr, target)
    if right - left == 0:
        print(0)
    else:
        print(1)
