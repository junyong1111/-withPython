import sys
sys.stdin = open("9.알고리즘유형별/그리디/input.txt")

N, M = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(N-1):
    target = weights[i]
    for j in range(i+1, N):
        if target != weights[j]:
            answer +=1
print(answer)