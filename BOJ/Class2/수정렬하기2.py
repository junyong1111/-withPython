import sys
# sys.stdin = open("BOJ/Class2/input.txt")

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readlines()))

arr = sorted(arr)
for i in range(n):
    print(arr[i], end="\n")