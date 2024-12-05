from math import gcd

def calculate_min_floor(n, m, elevators):
    min_floor = float('inf')
    
    for u, d in elevators:
        # 최대공약수와 최소공배수 계산
        gcd_val = gcd(u, d)
        uc = d // gcd_val  # == lcm(u, d) / u
        dc = u // gcd_val  # == lcm(u, d) / d
        zero_sum = uc + dc  # 주기 내 버튼 수
        
        # n % zero_sum 계산
        if n % zero_sum == 0:
            new_n = zero_sum
        else:
            new_n = n % zero_sum

        # 주기 내 남은 버튼 계산
        now_floor = 0
        while new_n > 0:
            if now_floor - d <= 0:  # 음수 방지
                now_floor += u
            else:
                now_floor -= d
            new_n -= 1

        # 최솟값 갱신
        min_floor = min(min_floor, now_floor)

    return min_floor

# 입력 처리
n, m = map(int, input().split())
elevators = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
print(calculate_min_floor(n, m, elevators))
