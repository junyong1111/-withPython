import sys
# sys.stdin = open("BOJ/Class2/input.txt")

def factorial(N):
    if N <= 1:
        return 1
    else:
        return (factorial(N-1) * N)
    
N, K = map(int, sys.stdin.readline().split())
if K == 0: #-- K 가 0인 경우
    print(1)
    sys.exit()
if K<=N:
    print(factorial(N) // (factorial(K)*factorial(N-K)))    
