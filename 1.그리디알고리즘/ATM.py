import sys
# sys.stdin = open('1.그리디알고리즘/input.txt')
n = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
#-- 가장 빨리 끝나는 사람 순으로 
people.sort()
for i in range(1, len(people)):
    people[i] = people[i] + people[i-1]
print(sum(people))