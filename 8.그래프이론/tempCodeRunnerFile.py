
def topology_sort():
    q = deque()
    ret = []
    
    for i in range(1, number+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q :
        now = q.popleft()
        
        for nnode in subjects[now]:
            indegree[nnode] -= 1
            if indegree[nnode] == 0:
                q.append(nnode)
                ret.append(nnode)
    return ret

result = topology_sort()
print(result)

    