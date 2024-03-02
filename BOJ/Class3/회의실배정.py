import sys
sys.stdin = open("BOJ/Class3/input.txt")

n = int(sys.stdin.readline())
MAX_SIZE = 100001
rooms = [()]
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    rooms.append((a,b))

rooms.sort(key=lambda x : x[1])
