
from collections import deque

M, N, H = map(int, input().split())

total_boxes = [[[] for _ in range(N)] for _ in range(H)]
for h in range(H):
    for n in range(N):
        total_boxes[h][n] = list(map(int, input().split()))


def bfs_tomato(total_boxes):
    H, N, M = len(total_boxes), len(total_boxes[0]), len(total_boxes[0][0])
    q = deque()
    # 앞,뒤,좌,우,상,하
    dh = [0, 0, 0, 0, 1, -1]
    dr = [1, -1, 0, 0, 0, 0]
    dc = [0, 0, -1, 1, 0, 0]
    # 초기 익은 토마토를 모두 큐에 넣기
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if total_boxes[h][r][c] == 1:
                    q.append((h, r, c, 0))  # day도 같이 저장
    max_day = 0
    # BFS
    while q:
        now_h, now_r, now_c, day = q.popleft()
        max_day = max(max_day, day)
        for i in range(6):
            nr = now_r + dr[i]
            nc = now_c + dc[i]
            nh = now_h + dh[i]
            if (0 <= nr < N and 0 <= nc < M and 0 <= nh < H and total_boxes[nh][nr][nc] == 0):
                total_boxes[nh][nr][nc] = 1
                q.append((nh, nr, nc, day + 1))

        # BFS 후 안 익은 토마토가 있으면 -1
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if total_boxes[h][r][c] == 0:
                    return -1
    return max_day


result = bfs_tomato(total_boxes)
print(result)
