from collections import deque
def solution(maps):
    
    # distance = [[0]*len(maps[0]) for _ in range(len(maps))] 
    
    
    n = len(maps)
    m = len(maps[0])
    distance = [[0 for _ in range(m)]  for _ in range(n)]
	
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    ## 처음 시작값을 큐에 삽입
    
    find = deque([(0, 0)]) 
    maps[0][0] = 0
    distance[0][0] = 1 ## 시작점은 1로
    
    
    while find:
        x,y = find.popleft()
        
        ## 네 방향 확인
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            ### 범위안에 있으면서 벽이 아닌경우 ##
            if 0 <= X < len(maps[0]) and 0 <= Y < len(maps) and maps[Y][X] == 1:
                maps[Y][X] = 0 ## 중복을 막기 위해 현재위치 벽으로 지정
                distance[Y][X] = distance[y][x] + 1 ## 이전 위치 +1 
                find.append((X,Y))
        
        
    if distance[n-1][m-1] == 0: ## 목적지에 도달하지 못함
        return -1
    else :
        return distance[n-1][m-1]