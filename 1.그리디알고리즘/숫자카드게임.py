import sys

sys.stdin = open('1.그리디알고리즘/input.txt')
n, m = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

max_value = 0
for i in range(n):
    if max_value <= min(arr[i]):
        max_value = min(arr[i])
print(max_value)