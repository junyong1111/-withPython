import sys
sys.stdin = open("BOJ/Class3/input.txt")

MAX_SIZE = 301

n = int(sys.stdin.readline())
stairs = []
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

