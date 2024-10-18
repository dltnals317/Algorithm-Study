# min 계속 초기화

from collections import deque


N,M = map(int,input().split())

maze = [list(map(int,input())) for _ in range(N)]

#좌,상,우,하
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 방문 여부 확인 배열
visited = [[False] * M for _ in range(N)]
# 큐 생성 및 시작점 추가
queue = deque([(0, 0, 1)])
visited[0][0] = True  # 시작점 방문 처리


while queue:
    (i,j,r) = queue.popleft()
    
     # 도착 지점에 도달한 경우 경로 길이 출력 후 종료
    if i == N - 1 and j == M - 1:
        break
    for k in range(4):
        nx = j + dx[k]
        ny = i + dy[k]
        if 0<= nx < M and 0 <= ny < N and maze[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True  # 방문 처리
            queue.append((ny,nx,r+1))
     
print(r)          
            