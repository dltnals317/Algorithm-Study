N = int(input())

# DP 테이블 초기화
dp = [0] * (N+1)
# 다이나믹 프로그래밍 진행(bottom-up)
for i in range(2, N+1): # i=2,3,4,5,6,7,8,9,10
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i-1] + 1 #dp[2] = dp[1] + 1 = 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    


# 결과 출력
print(dp[N])