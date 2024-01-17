import sys
# sys.stdin = open("input.txt")

# 1 2 3 4 5 6 7
n, k  = map(int, sys.stdin.readline().split())
people = [i for i in range(1, n+1)]

idx = k-1    
print("<", end="")
for i in range(n-1):
    print(people[idx], end=", ") #-- k번째 출력
    people.pop(idx)
    idx = (idx+ k-1) % len(people)
    #//현재 인덱스 + 주어진 위치 % 배열의 크기 이래야 원형으로 순환가능    
print(people[-1], end="")
print(">")