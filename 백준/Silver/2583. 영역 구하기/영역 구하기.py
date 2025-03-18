from collections import deque
M,N,K = map(int,input().split())


board= [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

#좌,상,우,하
dr = [0,-1,0,1]
dc = [-1,0,1,0]


# 색칠 -> 1
for _ in range(K):
    r1,c1,r2,c2 = map(int,input().split()) #1은 왼쪽 아래, 2는 오른쪽 위
    for r in range(r1,r2): #1~4
        for c in range(c1,c2):
            if board[r][c] == 0:
                board[r][c] = 1
cnt = 0
area_lst = []

def bfs(row,col):
    queue = deque()
    queue.append((row,col))
    visited[row][col] = True
    area = 1

    while queue:
        now_r,now_c = queue.popleft()
        #visited[now_r][now_c] = True
        for i in range(4):
            nr = dr[i] + now_r
            nc = dc[i] + now_c
            if (0<= nr <N and 0<=nc<M) and board[nr][nc] == 0 and visited[nr][nc] == False: 
                queue.append((nr,nc))
                visited[nr][nc] = True
                area+=1
                

    
    area_lst.append(area)
    
for row in range(N): #(0,0),(0,1)...
    for col in range(M):
        if visited[row][col] == False and board[row][col] == 0:
            bfs(row,col)
            cnt+=1
        
            
area_lst.sort()       
print(cnt)
for i in area_lst:
    print(i, end = " ")