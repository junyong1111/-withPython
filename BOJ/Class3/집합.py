import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline
MAX_SIZE = 20
# -- 모든 조건이 상수 처리

S = dict()
N = int(input())

while N:
    N -= 1
    order = input().split()
    if order[0] == "add":
        S[int(order[1])] = 1
    elif order[0] == "remove":
        if int(order[1]) in S:
            S.pop(int(order[1]))
    elif order[0] == "check":
        if int(order[1]) in S:
            print(1)
        else:
            print(0)
    elif order[0] == "toggle":
        if int(order[1]) in S:
            S.pop(int(order[1]))
        else:
            S[int(order[1])] = 1
    elif order[0] == "all":
        S.clear()
        for i in range(1, MAX_SIZE+1):
            S[i] = 1
    elif order[0] == "empty":
        S.clear()
