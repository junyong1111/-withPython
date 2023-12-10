
import sys
sys.setrecursionlimit(6)
sys.stdin = open("8.그래프이론/input.txt")

node, edge = map(int, sys.stdin.readline().split())

### step1. 부모 테이블 초기화
### Step2. 재귀적으로 부모 찾기
### Step3. 찾은 값에 맞게 테이블 갱싱

table = [0] * (node+1)
#-- 초기설정 : 자기자신의 부모노드는 자기자신 
for i in range(node+1):
    table[i] = i
# [0, 1, 2, 3, 4, 5, 6]


def findParent(node, table): #-- 경로 압축 기법 적용
    if table[node] != node:
        table[node] = findParent(table[node], table)
    return table[node]

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    parent_a = findParent(a, table)
    parent_b = findParent(b, table)
    
    if parent_a < parent_b:
        table[parent_b] = parent_a
    else:
        table[parent_a] = parent_b


print('각 원소가 속한 집합: ', end='')
for i in range(1, node+1):
    print(findParent(i, table), end=" ")
print()

print('부모 테이블 : ', end='')
for i in range(1, node+1):
    print(table[i], end= ' ')
