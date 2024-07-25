from collections import deque
N = int(input())
ground=[list(map(int,input().split())) for _ in range(N)]

d_right = [0,1]
d_down = [1,0]


value = ground[0][0]
now = (0,0)
q = deque()
q.append(now)

result = 0
cnt=0
visited = []

while q:
    i,j = q.popleft()
    if i==N-1 and j == N-1:
        cnt+=1
        break
    value = ground[i][j]
    for x in range(2): #x=0,1
        new_i,new_j = i+value*d_down[x], j+value*d_right[x]
        if 0<=new_i <= N-1 and 0<=new_j <= N-1 and (new_i,new_j) not in visited:
            q.append((new_i,new_j))
            visited.append((new_i,new_j))
 

if cnt == 1:
    print("HaruHaru")
else:
    print("Hing")
