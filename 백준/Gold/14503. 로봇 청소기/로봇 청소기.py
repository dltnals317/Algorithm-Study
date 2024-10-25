N, M = map(int, input().split())
r, c, d = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

# 방향: 북(0), 동(1), 남(2), 서(3)
dr = [-1, 0, 1, 0]  # 행 이동
dc = [0, 1, 0, -1]  # 열 이동

cleaned_count = 0
end = False

while not end:
    if ground[r][c] == 0:  # 현재 칸이 청소되지 않은 경우
        ground[r][c] = 2  # 청소 완료 표시
        cleaned_count += 1  # 청소한 칸 카운트 증가

    all_around_clean = True

    # 네 방향 탐색
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 방향 회전
        nr, nc = r + dr[d], c + dc[d]

        # 청소되지 않은 빈 칸이 있는 경우
        if 0 <= nr < N and 0 <= nc < M and ground[nr][nc] == 0:
            r, c = nr, nc  # 이동
            all_around_clean = False
            break

    if all_around_clean:  # 네 방향 모두 청소된 경우
        # 후진
        nr, nc = r - dr[d], c - dc[d]
        if 0 <= nr < N and 0 <= nc < M and ground[nr][nc] != 1:  # 벽이 아니면 후진
            r, c = nr, nc
        else:  # 후진할 수 없으면 작동 종료
            end = True

print(cleaned_count)
