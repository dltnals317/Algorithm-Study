N = int(input())

def rock_game():
    dp = [0]*1001
    dp[1], dp[2] = 1, 2

    for i in range(3, N+1):
        dp[i] = dp[i-1]+1
    
    # 횟수가 짝수면 CY, 홀수면 SK가 승리한 것
    if dp[N] % 2:
        return 'SK'
    return 'CY'

print(rock_game())