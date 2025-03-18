from collections import deque

N = int(input())

board = []
for _ in range(N):
    row_lst = board.append(list(map(int,input())))


visited = [[False]*N for _ in range(N)]

#좌,상,우,하
dr = [0,-1,0,1]
dc = [-1,0,1,0]

total = 0
group_lst = []
def bfs(row,col):
    queue = deque()
    visited[row][col] = True
    queue.append((row,col))
    group_sum= 1 
    while queue:
        now_row,now_col = queue.popleft()
        for i in range(4):
            nr = now_row + dr[i]
            nc = now_col + dc[i]
            if ((0<= nr < N and 0 <= nc < N) and board[nr][nc] == 1 and visited[nr][nc] == False):
                queue.append((nr,nc))
                visited[nr][nc] = True
                group_sum+=1
    
    
    group_lst.append(group_sum)
    

for row in range(N):
    for col in range(N):
        if visited[row][col] == False and board[row][col] == 1:
            bfs(row,col)
            total+=1
            

print(total)
group_lst.sort()
for cnt in group_lst:
    print(cnt)