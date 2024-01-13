import sys
import math
# sys.stdin = open("BOJ/Class2/input.txt")

def maxSwap(a, b, c):
    if a>=b and a>=c:
        return b, c, a
    if b>=a and b>=c:
        return a, c, b
    return a, b, c
    
while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    a, b, c = maxSwap(a, b, c)
    
    if int(math.pow(a, 2)) + int(math.pow(b, 2)) == int(math.pow(c, 2)):
        print("right")
    else:
        print("wrong")