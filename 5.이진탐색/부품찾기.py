import sys
import bisect
from bisect import bisect_left as left
from bisect import bisect_right as right


sys.stdin = open("5.이진탐색/input.txt")
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
# print(arr)
m = int(sys.stdin.readline().rstrip())
targets = list(map(int, sys.stdin.readline().split()))

for target in targets:
    ret = right(arr, target) - left(arr, target)
    if ret == 0:
        print('no', end=' ')
    else:
        print("yes", end= ' ')


