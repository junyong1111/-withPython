import sys
sys.stdin = open("4.정렬/input.txt")

n = int(sys.stdin.readline())

info = []

for i in range(n):
    data = sys.stdin.readline().split()
    info.append((data[0], data[1]))

info = sorted(info, key = lambda students : students[1])
for data in info:
    print(data[0], end =" ")
