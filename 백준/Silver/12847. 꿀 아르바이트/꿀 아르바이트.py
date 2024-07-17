n, m = map(int, input().split())
pay = list(map(int, input().split()))

# 첫 윈도우의 합 계산
current_sum = sum(pay[:m])
max_sum = current_sum

# 슬라이딩 윈도우 적용
for i in range(m, n):
    current_sum = current_sum - pay[i - m] + pay[i]
    max_sum = max(current_sum, max_sum)

print(max_sum)

