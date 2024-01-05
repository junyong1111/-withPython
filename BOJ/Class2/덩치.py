import sys
# sys.stdin = open("input.txt")

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    rank = 1
    weight, height = people[i]
    for j in range(n):
        if i == j:
            continue
        if weight<people[j][0] and height<people[j][1]: #-- 나보다 덩치 큰 사람이 존재하면 1단계 내려감
            rank+=1
    print(rank, end=" ")