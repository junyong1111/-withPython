import sys
import math
# sys.stdin = open("input.txt")
M, N = map(int, sys.stdin.readline().split())

#-- 어떤수의 제곱을 구할 때 해당값이 int자료형을 넘어갈 수 있으므로 long long 으로 자료형을 지정해줘야 함
def isPrime(number):
    if number <= 1:
        return False
    i = 2
    while i*i <= number:
        if number % i ==0:
            return False
        i+=1
    return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)