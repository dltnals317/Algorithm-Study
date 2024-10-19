def solution(n):
    tmp_map = [[0] * n for _ in range(n)]  # n x n 크기의 배열 생성
    number = 1  # 숫자는 1부터 시작
    direction = "right"
    now = (0, 0)  # 시작 좌표
    top, bottom = 0, n - 1  # 위쪽과 아래쪽 경계
    left, right = 0, n - 1  # 왼쪽과 오른쪽 경계

    while number <= n * n:  # 숫자가 n^2까지 반복
        if direction == "right":  # 오른쪽으로 이동
            for j in range(left, right + 1):
                if tmp_map[now[0]][j] != 0:
                    break
                tmp_map[now[0]][j] = number
                number += 1
            top += 1  # 위쪽 경계를 한 칸 아래로 내림
            now = (top, right)  # 현재 위치 업데이트
            direction = "down"
        elif direction == "down":  # 아래쪽으로 이동
            for i in range(top, bottom + 1):
                if tmp_map[i][now[1]] != 0:
                    break
                tmp_map[i][now[1]] = number
                number += 1
            right -= 1  # 오른쪽 경계를 한 칸 왼쪽으로 줄임
            now = (bottom, right)  # 현재 위치 업데이트
            direction = "left"
        elif direction == "left":  # 왼쪽으로 이동
            for j in range(right, left - 1, -1):
                if tmp_map[now[0]][j] != 0:
                    break
                tmp_map[now[0]][j] = number
                number += 1
            bottom -= 1  # 아래쪽 경계를 한 칸 위로 올림
            now = (bottom, left)  # 현재 위치 업데이트
            direction = "up"
        elif direction == "up":  # 위쪽으로 이동
            for i in range(bottom, top - 1, -1):
                if tmp_map[i][now[1]] != 0:
                    break
                tmp_map[i][now[1]] = number
                number += 1
            left += 1  # 왼쪽 경계를 한 칸 오른쪽으로 이동
            now = (top, left)  # 현재 위치 업데이트
            direction = "right"

    # 결과 출력
    for row in tmp_map:
        print(row)

    return tmp_map
