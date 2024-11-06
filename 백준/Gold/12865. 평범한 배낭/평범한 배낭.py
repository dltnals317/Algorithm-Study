N,K = map(int,input().split())

weight_value_lst = [(0,0)]

for _ in range(N):
    w,v = map(int,input().split())
    weight_value_lst.append((w,v))
dp = [[0]*(K+1) for i in range(N+1)]


for i in range(1,N+1):
    for j in range(1,K+1): # j는 가능한 무게
        item_weight,item_value = weight_value_lst[i][0],weight_value_lst[i][1] #i번째 아이템
        if j < item_weight: #못넣음
            dp[i][j] = dp[i-1][j]
        elif j >= item_weight:
            dp[i][j] = max(dp[i-1][j-item_weight] + item_value,dp[i-1][j])


print(dp[-1][-1])
        
    
