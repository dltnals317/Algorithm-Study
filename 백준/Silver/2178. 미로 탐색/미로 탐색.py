from collections import deque

N,M = map(int,input().split())
road = [list(map(int,input())) for _ in range(N)]

def miro_bfs():
  visited = [[False]*M for _ in range(N)]
  q = deque([((0,0),1)])
  visited[0][0] = True
  

  #상,좌,하,우
  dr = [-1,0,1,0]
  dc = [0,-1,0,1]
  
  temp = []

  while q:
    (r,c),d = q.popleft()
    
    
    for i in range(4):
      n_r = r + dr[i]
      n_c = c + dc[i]
      if (n_r,n_c) == (N-1,M-1):
        temp.append(d+1)
        
        break
      
      #벽이거나 이미 방문한 노드라면
      if (0 <= n_r < N and 0 <= n_c < M) == False or visited[n_r][n_c] == True:
        continue
      
      if road[n_r][n_c] == 1:
        visited[n_r][n_c] = True
        q.append(((n_r,n_c),d+1))

  return temp
  
result = miro_bfs()
print(min(result))
