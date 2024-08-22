#각 위치에서는, max(내 왼쪽 위까지합 , 내 오른쪽 위까지 합)

def solution(triangle):
    
    dp = []
    for lst in triangle:
        dp.append([0] * len(lst)) #	[[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
    dp[0][0] = triangle[0][0]
    #왼쪽 빗면,오른쪽 빗면은 한쪽 방향에서만 내려옴
    for i in range(1,len(triangle)): #	[[7], [10, 15], [18, 0, 15], [20, 0, 0, 19], [24, 0, 0, 0, 24]]
        dp[i][0]= triangle[i][0] + dp[i-1][0]
        dp[i][-1]= triangle[i][-1] + dp[i-1][-1]
    
    for i in range(1,len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1],dp[i-1][j])
            
    

    answer = max(dp[-1])
    return answer