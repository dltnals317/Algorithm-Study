#1. 현재 빙하 덩어리 수 센다. 언제까지? 빙하 덩어리 수가 1보다 커질 때까지
# 빙하 덩어리 수 == 1 -> bfs로 얼마나 녹을지 파악 -> melt함수로 파악한거 한번에 녹여 -> day+1
# 다시 덩어리 수 세.
# "빙산이 두 개 이상으로 나뉘지 않고 전부 녹은 경우" 도 생각해야함

from collections import deque

N, M = map(int, input().split())

area_input = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*(M) for _ in range(N)]
# 좌 상 우 하

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]
def bfs(r,c,visited,melt_info):
    q = deque([(r,c)])
    visited[r][c] = True

    while q:
        now_r,now_c = q.popleft()
        sea_cnt_around_now = 0
        for i in range(4):
            n_r = now_r + dr[i]
            n_c = now_c + dc[i]
            if (0<=n_r<N and 0<=n_c<M ):
                if area_input[n_r][n_c] == 0:
                    sea_cnt_around_now+=1
                elif (area_input[n_r][n_c] !=0 and visited[n_r][n_c] == False):
                    q.append((n_r,n_c))
                    visited[n_r][n_c] = True
        melt_info.append((now_r, now_c, sea_cnt_around_now)) #now_r,now_c 지점에서 sea_cnt_around_now만큼 녹이겠다!


def melt(melt_info):
    for r,c,height in melt_info:
        area_input[r][c] = max(0,area_input[r][c] - height)




def count_chunks():
    visited = [[False] * M for _ in range(N)]  # visited는 매번 새로
    chunk_cnt = 0
    melt_info = []
    for r in range(N):
        for c in range(M):
            if area_input[r][c] !=0 and visited[r][c] == False: #방문 아직 안한 첫 빙산(바다X) 발견 -> 그 빙산 기점으로, 영향 받는 주변 친구들 확인해야함. 거기까지가 chunks니까!어떻게? bfs로!
                bfs(r,c,visited,melt_info) # 이 bfs로 인해, (r,c) 주변애들, 또 그 주변에들은 방문 상태가 됨!
                #그럼에도 for문 돌아서 다시 if에 걸린다면=> 걔는 아까 만난 그 무리가 아닌거.
                chunk_cnt+=1
    # chuck갯수 다 셋으면, 일 단 한번 녹이자
    melt(melt_info)
    return chunk_cnt

day = 0
while True:
    chunks = count_chunks()
    if chunks == 0:
        print(0)
        break
    if chunks >=2 :
        print(day)
        break
    day+=1
#이렇게 해버리면 => 프로그램 시작 시 딱 한 번만 count_chunks()를 호출->그 시점의 빙산 덩어리 개수만 센다 -> melt기능 필요
# result = count_chunks(0)
# print(result)
