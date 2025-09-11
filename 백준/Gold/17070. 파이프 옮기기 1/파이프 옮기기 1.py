N = int(input())


arr_map = [list(map(int,input().split())) for _ in range(N)]

#방향 추가
dp = [[[0]*(3) for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1 #(0,1)위치 & 가로

for r in range(N):
    for c in range(N):

        #1. 수직 이동
        if r+1 < N and arr_map[r+1][c] == 0:
            dp[r+1][c][1] += dp[r][c][1]
        if c+1 < N and r+1 < N and arr_map[r+1][c+1] == 0 and arr_map[r][c+1] == 0 and arr_map[r+1][c] == 0:
            dp[r+1][c+1][2] +=dp[r][c][1] #대각선
        
        #2. 수평 이동
        if c+1 < N and arr_map[r][c+1] == 0:
            dp[r][c+1][0] += dp[r][c][0]
        if r+1 < N and c+1 < N and arr_map[r+1][c+1] == 0 and arr_map[r][c+1] == 0 and arr_map[r+1][c] == 0:
            dp[r+1][c+1][2] +=dp[r][c][0] #대각선

        #3. 대각선 이동
        if c+1 < N and arr_map[r][c+1] == 0:
            dp[r][c+1][0] += dp[r][c][2]
        if r+1 < N and arr_map[r+1][c] == 0:
            dp[r+1][c][1] += dp[r][c][2]
        if r+1 < N and c+1 < N and arr_map[r+1][c+1] == 0 and arr_map[r][c+1] == 0 and arr_map[r+1][c] == 0:
            dp[r+1][c+1][2] +=dp[r][c][2] #대각선

result = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]        
            
print(result)