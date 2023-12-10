import sys
from collections import deque
import copy
sys.stdin = open('8.그래프이론/input.txt')

number = int(sys.stdin.readline())
indegree = [0] * (number + 1)
subjects = [0] * (number + 1)
graph = [[] for _ in range(number+1)]


for i in range(1, number+1):
    data = sys.stdin.readline().split()
    for j in range(len(data)):
        value = int(data[j])
        if j == 0:
            subjects[i] = value
        elif value != -1:
            graph[value].append(i)
            indegree[i] +=1
        else:
            break
            

def topology_sort():
    q = deque()
    ret = copy.deepcopy(subjects)
    
    for i in range(1, number+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q :
        now = q.popleft()
        
        for nnode in graph[now]:
            ret[nnode] = max(ret[nnode], ret[now] + subjects[nnode])
            indegree[nnode] -= 1
            if indegree[nnode] == 0:
                q.append(nnode)
    return ret


result = topology_sort()
for i in range(1, number+1):
    print(result[i])