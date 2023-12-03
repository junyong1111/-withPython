import sys
import bisect
from bisect import bisect_left, bisect_right
# sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

cards = sorted(cards)

for target in targets:
    left, right = bisect_left(cards, target), bisect_right(cards, target)
    print(right-left, end = ' ')