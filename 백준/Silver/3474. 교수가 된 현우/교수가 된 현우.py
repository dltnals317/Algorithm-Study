N = int(input())  # 테스트 케이스 수
for _ in range(N):
    num = int(input())  # 각 테스트 케이스에서 입력받은 N
    cnt = 0
    i = 5
    while i <= num:
        cnt += num // i #5를 인수로 가지는 갯수, 5^2를 인수로 가지는 갯수,5^3를 인수로 가지는 갯수...
        i *= 5
    print(cnt)
