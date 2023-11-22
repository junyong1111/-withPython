# def ispossible()
def solution(n, lost, reserve):
    answer = 0
    
    arr = []
    for i in range(n+1):
        arr.append(1)
        
    for l in lost:
        arr[l] = arr[l]-1
        
    for r in reserve:
        arr[r] = arr[r] +1
        
    for i in range(1, n+1):
        if arr[i] != 2: #-- 체육복 여분 없으면 넘어감
            continue
        left = i -1
        right = i+1
        if left != 0 and arr[left] == 0:
            arr[left] = arr[left] +1 
            arr[i] = arr[i] -1
            continue
        if right != n+1 and arr[right] == 0:
            arr[right] = arr[right] +1
            arr[i] = arr[i] - 1
    
    for i in range(1, n+1):
        if arr[i] >=1:
            answer = answer + 1
         
    return answer