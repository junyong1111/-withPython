import sys

# sys.stdin = open("BOJ/Class2/input.txt")
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

setA = set(A) #-- 선형시간 탐색을 위한 

for data in B:
    if data in setA:
        print(1)
    else:
        print(0)