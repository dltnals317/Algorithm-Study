# 상(북), 우(동), 하(남), 좌(서)
dr = [-1, 0, 1, 0] 
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, sight = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

def now_clean(row, col, lst):
    global cnt
    if lst[row][col] == 0:  # 현재 칸이 청소되지 않았다면
        lst[row][col] = 2  # 현재 칸을 청소 (2는 청소 완료 상태)
        cnt += 1

def around_check_and_action(row, col, sight, lst):
    now_clean(row, col, lst)  # 현재 칸 청소
    
    for _ in range(4):  # 4 방향 회전
        new_sight = (sight + 3) % 4  # 반시계 방향으로 회전
        nr = row + dr[new_sight]
        nc = col + dc[new_sight]
        
        if 0 <= nr < N and 0 <= nc < M :
            if lst[nr][nc] == 0:  # 청소되지 않은 빈 칸이 있을 때
                around_check_and_action(nr, nc, new_sight, lst)
                return
        
        sight = new_sight  # 다음 회전을 위해 방향 업데이트
    
    # 네 방향 모두 청소된 경우 후진
    back_dir = (sight + 2) % 4  # 현재 방향의 반대 방향
    nr = row + dr[back_dir]
    nc = col + dc[back_dir]
    if 0 <= nr < N and 0 <= nc < M and lst[nr][nc] != 1:  # 벽이 아닐 때
        around_check_and_action(nr, nc, sight, lst)

# 로봇 청소 시작
around_check_and_action(r, c, sight, room)

# 최종 청소한 칸의 수 출력
print(cnt)
