'''
1. N에서 1을 뺀다
2. N을 K로 나눈다. => N이 K로 나누어 떨어질 때만 선택 가능
'''
import sys
sys.stdin = open('1.그리디알고리즘/input.txt')
n, k = map(int, sys.stdin.readline().split())
# print(n, k)

cnt = 0
while n != 1:
    if n % k == 0:
        n = n//k
        cnt += 1
    else:
        n = n -1
        cnt +=1
print(cnt)