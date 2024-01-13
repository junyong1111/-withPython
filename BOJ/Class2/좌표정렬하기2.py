import sys
# sys.stdin = open("BOJ/Class2/input.txt")

n = int(sys.stdin.readline())
points = []

for _ in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))

points = sorted(points, key=lambda point :(point[1], point[0]))               
for point in points:
    print("{} {}".format(point[0], point[1]))