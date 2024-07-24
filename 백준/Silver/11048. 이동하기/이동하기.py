# 1행, 1열만 자기자신으로 초기화
#나머지부터는 해당 위치 + max(위,왼쪽,왼쪽 대각선 위)로 업데이트
#(r,c)의 값 출력


N,M = map(int,input().split())

ground = []
dp = [[0]*M for _ in range(N)]

for i in range(N):
    ground.append(list(map(int,input().split())))


dp[0][0] = ground[0][0]
#1행 초기화
for j in range(1,M):
    dp[0][j] = ground[0][j] + dp[0][j-1]


#1열 초기화
for i in range(1,N):
    dp[i][0] = ground[i][0] + dp[i-1][0]

for i in range(1,N):
    for j in range(1,M):
        dp[i][j] = ground[i][j] + max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])


print(dp[-1][-1])