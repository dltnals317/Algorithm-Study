D, K = map(int, input().split())
dp = [0] * D
dp[0] = "a"
dp[1] = "b"

# 피보나치 수열과 유사한 방식으로 문자열을 채우기
for i in range(2, D):
    dp[i] = dp[i-2] + dp[i-1]

# 마지막 날의 떡 개수에서 'a'와 'b'의 계수를 찾기
num_a = dp[-1].count('a')
num_b = dp[-1].count('b')

# A와 B의 값을 찾기
for A in range(1, K // num_a + 1):
    B = (K - num_a * A) // num_b
    if (K - num_a * A) % num_b == 0 and A <= B:
        print(A)
        print(B)
        break
