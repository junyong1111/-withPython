import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("6.다이나믹프로그래밍/input.txt")

n = int(sys.stdin.readline())

recursive_cnt = 0
dp_cnt = 0
def fib(n) :
    global recursive_cnt
    recursive_cnt = recursive_cnt+1
    if (n == 1) or (n == 2):
        return 1; 
    else :
        return (fib(n - 1) + fib(n - 2))

dp = [0] * 41
dp[1] = 1 
dp[2] = 1
def fibonacci(n) :
    global dp_cnt
    dp_cnt = dp_cnt +1
    if dp[n] != 0:
        return dp[n]
    else:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

fib(n)
fibonacci(n)

print(recursive_cnt)
print(dp_cnt)