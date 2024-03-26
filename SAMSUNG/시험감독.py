import sys
import math
# sys.stdin = open("SAMSUNG/input.txt")

input = sys.stdin.readline
N = int(input())
testRoom = list(map(int, input().split()))

B, C = map(int, input().split())

answer = 0

for test in testRoom:
    people = test - B
    answer+=1

    if people<=0:
        continue
    answer += math.ceil(people/C)
print(answer)