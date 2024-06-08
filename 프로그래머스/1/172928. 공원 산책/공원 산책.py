def solution(park, routes): #상,우,하,좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    park_lst = [list(p) for p in park]  
    
    W = len(park[0])  # 공원의 가로 길이
    H = len(park)     # 공원의 세로 길이
    
    # 현재 위치 찾기
    for i in range(H):
        for j in range(W):
            if park_lst[i][j] == "S":
                now_x, now_y = i, j
    
    for command in routes:
        direction = command[0]
        distance = int(command[2:])
        if direction == 'N':
            nx = now_x - distance
            ny = now_y
        elif direction == 'S':
            nx = now_x + distance
            ny = now_y
        elif direction == 'W':
            nx = now_x
            ny = now_y - distance
        elif direction == 'E':
            nx = now_x
            ny = now_y + distance 
            
        # 이동 가능한지 확인
        blocked = False
        if 0 <= nx < H and 0 <= ny < W:
            if direction in ['E', 'W']:
                for i in range(min(now_y, ny), max(now_y, ny) + 1):
                    if park_lst[nx][i] =='X':
                        blocked = True
                        break
                    
            elif direction in ['S', 'N']:
                for i in range(min(now_x, nx), max(now_x, nx) + 1):
                    if park_lst[i][ny] =='X':
                        blocked = True
                        break
                    
            if not blocked:
                now_x, now_y = nx, ny
                
    return (now_x, now_y)
