from collections import deque

N,M = map(int,input().split())

area = []
for i in range(M):
    area.append(list(input()))


d_i = [-1,1,0,0] #상,하,좌,우
d_j = [0,0,-1,1]

visited = [[False]* N for _ in range(M)]

q_w = deque()
q_b = deque()

result_W = []
result_B = []
for x in range(M):
    for y in range(N):
        if area[x][y] == "W":
            if visited[x][y] == False:
                cnt = 1
                visited[x][y] = True
                q_w.append((x,y))
                while q_w:
                    i,j = q_w.popleft()
                    for k in range(4):
                        new_i = i + d_i[k]
                        new_j = j + d_j[k]
                        if 0 <= new_i < M and 0<=new_j<N and area[new_i][new_j] == "W":
                            if visited[new_i][new_j] == False:
                                q_w.append((new_i,new_j))
                                visited[new_i][new_j] = True
                                cnt += 1
                result_W.append(cnt)
            
        elif area[x][y] == "B":
            if visited[x][y] == False:
                cnt = 1
                visited[x][y] = True
                q_b.append((x,y))
                while q_b:
                    i,j = q_b.popleft()
                    for k in range(4):
                        new_i = i + d_i[k]
                        new_j = j + d_j[k]
                        if 0 <= new_i < M and 0<=new_j<N and area[new_i][new_j] == "B":
                            if visited[new_i][new_j] == False:
                                q_b.append((new_i,new_j))
                                visited[new_i][new_j] = True
                                cnt += 1
                result_B.append(cnt)

W = 0
B = 0
for x in result_W:
    W+= x*x
for x in result_B:
    B+= x*x

print(W,B,sep=" ")
