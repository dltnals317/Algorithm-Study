def solution(park, routes): #상,우,하,좌
    H = len(park)
    W = len(park[0])
    d_row = [-1,1]
    d_col = [-1,1]
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                now_row,now_col = i,j 
                
    for rt in routes:
        direction,length= rt.split()
        if direction == 'E': #동 -> j의 이동
            n_row = now_row
            n_col = now_col + (d_col[1]*int(length))
        elif direction =='S': #남 -> i의 이동
            n_row = now_row + (d_row[1]*int(length))
            n_col = now_col
        elif direction == 'W': #서 -> j의 이동
            n_row = now_row
            n_col = now_col + (d_col[0]*int(length))
        elif direction == 'N': #북
            n_row = now_row + (d_row[0]*int(length))
            n_col = now_col
        
        blocked = False
        # 남쪽 또는 북쪽으로 이동하는 경우
        if direction == 'S':
            for i in range(now_row + 1, n_row + 1):
                if i < 0 or i >= H or park[i][now_col] == 'X':
                    blocked = True
                    break
        elif direction == 'N':
            for i in range(now_row - 1, n_row - 1, -1):
                if i < 0 or i >= H or park[i][now_col] == 'X':
                    blocked = True
                    break
        
        # 동쪽 또는 서쪽으로 이동하는 경우
        elif direction == 'E':
            for j in range(now_col + 1, n_col + 1):
                if j < 0 or j >= W or park[now_row][j] == 'X':
                    blocked = True
                    break
        elif direction == 'W':
            for j in range(now_col - 1, n_col - 1, -1):
                if j < 0 or j >= W or park[now_row][j] == 'X':
                    blocked = True
                    break
        
        if blocked:
            continue
        else:
            now_row, now_col = n_row, n_col
    
    result = [now_row, now_col]
    return result