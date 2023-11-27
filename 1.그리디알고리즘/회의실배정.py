import sys
# sys.stdin = open('1.그리디알고리즘/input.txt')
n = int(sys.stdin.readline())
looms = []
for i in range(n):
    looms.append(tuple(map(int, sys.stdin.readline().split())))

looms = sorted(looms, key= lambda loom : (loom[1], loom[0]))
answer = 1
finished = looms[0][1]
looms.pop(0)

for loom in looms:
    if finished <= loom[0]:
        finished = loom[1]
        answer += 1
print(answer)