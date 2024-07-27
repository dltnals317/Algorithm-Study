N = int(input())

stair = []
for i in range(N): #계단 리스트
    st = int(input())
    stair.append(st)


dp = [0] * N #dp는 해당 지점까지의 최대 점수

if len(stair)<=2:
    print(sum(stair))

else:
    dp[0] = stair[0]
    dp[1] = stair[0] + stair[1]
    for i in range(2,len(stair)):
        dp[i] = max(dp[i-2]+stair[i] , dp[i-3] +stair[i-1]+ stair[i])

    print(dp[-1])
        
        
