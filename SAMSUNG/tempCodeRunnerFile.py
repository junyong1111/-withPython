if t == time:
        #-- L : 현재 진행에서 왼쪽으로 90도
        if direction == "L":
            dir = (dir-1)%4
        #-- D : 현재 진행에서 오른쪽으로 90도 방향 회전
        else:
            dir = (dir+1)%4
        if len(moves) != 0:
            t, direction = moves.popleft()