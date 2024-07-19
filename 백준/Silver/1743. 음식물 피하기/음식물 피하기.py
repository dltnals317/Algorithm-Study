from collections import deque
N,M,K = map(int,input().split())
ground = [[0]*M for _ in range(N)]

for i in range(K):
    r,c = map(int,input().split())
    ground[r-1][c-1] = 1
    
dr = [-1,0,1,0] #상,우,하,좌
dc = [0,1,0,-1]  #상,우,하,좌


q = deque()

max_trash = 0
for r in range(N):
    for c in range(M):
        if ground[r][c] == 1:
            cnt=0
            q.append((r,c))
            while q:
                r,c = q.popleft()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0<=nr <=N-1 and 0<=nc <=M-1 and ground[nr][nc]==1:
                        ground[nr][nc]=0
                        q.append((nr,nc))
                        cnt+=1
            max_trash = max(max_trash,cnt)
print(max_trash)
                