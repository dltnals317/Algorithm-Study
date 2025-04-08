from collections import deque
F, S, G, U, D = map(int,input().split())
# 10 1 10 2 1
def bfs_elevator(now):
    #위,아래
    d_up =  [U,0]
    d_down = [0,-D]
    num = 0
    visited = [False]*(F+1)
    q = deque([(now,num)])
    #visited_floor.append(now) # 이렇게 되면 O(n)의 시간복잡도가 발생해서 시간초과가 난다. set을 쓰거나, visited[False]이걸 쓰자
    visited[now] = True
    while q:
        now_floor,click_num = q.popleft()
        if now_floor == G: #목표 층 만나면 종료
            return click_num

        for i in range(2):
            next_floor = now_floor + d_up[i] + d_down[i]
            if 0<next_floor<=F and visited[next_floor]== False:
                visited[next_floor]= True
                q.append((next_floor,click_num+1))
    return "use the stairs"
    #bfs 끝난 후
print(bfs_elevator(S))