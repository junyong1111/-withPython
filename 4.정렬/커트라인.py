import sys
sys.stdin = open("4.정렬/input.txt")

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr = sorted(arr, reverse=True)
prize = []
for i in range(k):
    prize.append(arr[i])

print(prize[len(prize)-1])
