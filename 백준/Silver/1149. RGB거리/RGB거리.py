#맨 위나 맨 아래는 정해져야, DP로 나아갈 수 있다
# 어차피 R,G,B 세 개의 경우니까, 1번을 기준으로 케이스분류 해도 되지 않을까..?
#앞에서 부터 가면,당장 눈 앞에 보이는 최솟값이 찐 최소비용의 경로가 아닐 수 있어
#마지막->위로 가보자.

N = int(input())
cost_list = []
for i in range(N):
    cost_list.append(list(map(int,input().split())))


dp = [[0,0,0] for _ in range(N)]

#맨 윗줄

#맨 아랫줄
dp[-1][0]=cost_list[-1][0]
dp[-1][1]=cost_list[-1][1]
dp[-1][2]=cost_list[-1][2]

for i in range(N-2,-1,-1):
    for j in range(3):
        if j == 0:
            dp[i][j] = cost_list[i][j] + min(dp[i+1][1],dp[i+1][2])
        elif j==1:
            dp[i][j] = cost_list[i][j] + min(dp[i+1][0],dp[i+1][2])
        else:
            dp[i][j] = cost_list[i][j] + min(dp[i+1][0],dp[i+1][1])
        

print(min(dp[0]))