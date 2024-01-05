import sys
# sys.stdin = open("input.txt")

n = int(sys.stdin.readline())
members = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))

members = sorted(members, key = lambda member : member[0])
for member in members:
    print("{} {}".format(member[0], member[1]))