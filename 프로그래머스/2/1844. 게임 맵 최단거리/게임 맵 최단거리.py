"""
1. x,y,누적거리 이렇게 계속 쌓아간다
2. bfs풀자. queue에 인접한애를 넣고, 걔를 꺼내는 식으로 하면서,,
3. 상대편 진영(n,m)이 되었을 때, 지금까지 도달한 거리애랑 비교애서 작은걸 계속 갱신
"""

from collections import deque
def solution(maps):
    #좌표 (좌,상,우,하)
    dr = [0,-1,0,1]
    dc = [-1,0,1,0]
    n,m = len(maps),len(maps[0])
    q = deque([(0,0,1)])
    visited = [[False]*m for _ in range(n)]
    possible_distance = []
    min_d = 10000
    while q:
        r,c,d = q.popleft()
        
        if r == n - 1 and c == m - 1:
            min_d = min(min_d, d)
            continue  # 현재 거리가 최소 거리라면 이후 탐색을 계속
    
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr <n and 0<= nc < m and maps[nr][nc] == 1:
                if visited[nr][nc] == False:
                    q.append((nr,nc,d+1))
                    visited[nr][nc] = True
                    
                    
            
    if min_d == 10000:
        return -1
    else:
        return min_d
        
