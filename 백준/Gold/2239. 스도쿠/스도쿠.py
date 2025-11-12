import sys
input = sys.stdin.readline

board = [list(map(int, input().strip())) for _ in range(9)]

row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
sub_used = [[False] * 10 for _ in range(9)]
blanks = []

# 초기 상태 등록
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num == 0:
            blanks.append((i, j))
        else:
            row_used[i][num] = True
            col_used[j][num] = True
            sub_used[(i // 3) * 3 + (j // 3)][num] = True

def solve(idx=0):
    if idx == len(blanks):
        for r in board:
            print(''.join(map(str, r)))
        sys.exit(0)  # 첫 해답 찾으면 바로 종료
    r, c = blanks[idx]
    s = (r // 3) * 3 + (c // 3)
    for num in range(1, 10):
        if not row_used[r][num] and not col_used[c][num] and not sub_used[s][num]:
            board[r][c] = num
            row_used[r][num] = col_used[c][num] = sub_used[s][num] = True

            solve(idx + 1)

            board[r][c] = 0
            row_used[r][num] = col_used[c][num] = sub_used[s][num] = False

solve()
