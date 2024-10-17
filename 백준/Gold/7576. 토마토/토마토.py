# while문이 끝났을 때, 0이 존재한다면 -1반환

"""
1. ground를 입력받는다
2. 이중 for문을 돌면서, 익은 토마토인 경우, 인접한 것 중 익지 않는 토마토를 기록한다(영향을 미칠 토마토)
익지 않은 토마토인 경우, pass

3. 다시 좌표를 돌면서, 익은 토마토의 경우, 주변에 영향을 미치고, day+1
영향을 받아 익게된 토마토 기준으로 다시 같은 방식으로 day+1

"""

from collections import deque,defaultdict



M,N = map(int,input().split())
box_lst = []
ripe_tomato_spot = deque()

#좌,상,우,하
dy = [0,-1,0,1]
dx = [-1,0,1,0]


for _ in range(N):
    box_lst.append(list(map(int,input().split())))


for i in range(len(box_lst)):
    for j in range(len(box_lst[i])):
        if box_lst[i][j] == 1:
            ripe_tomato_spot.append((i, j))
                    
day = 0      
while ripe_tomato_spot:
    for _ in range(len(ripe_tomato_spot)):
        i, j = ripe_tomato_spot.popleft()
        for k in range(4):
            nx = j + dx[k]
            ny = i + dy[k]
            if 0 <= nx < M and 0 <= ny < N and box_lst[ny][nx] == 0:
                box_lst[ny][nx] = 1
                ripe_tomato_spot.append((ny,nx))
    #for 루프가 끝나면, 그날 익은 모든 토마토가 큐에서 빠져나가고, 새로운 익은 토마토들이 큐에 들어가 있음
    if ripe_tomato_spot:
        day+=1
        
for row in box_lst:
    if 0 in row:
        print(-1)  # 익지 않은 토마토가 남아 있으면 -1 출력
        exit()

# 모든 토마토가 익었다면 걸린 일수 출력
print(day)
        