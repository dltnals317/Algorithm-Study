N = int(input())  # 사람의 수
heights = list(map(int, input().split()))  # 각 사람의 왼쪽 키 큰 사람 수

result = [0] * N  # 결과를 저장할 리스트

for i in range(N):
    count = heights[i]  # 왼쪽에 있어야 하는 키 큰 사람의 수
    for j in range(N):
        if result[j] == 0:  # 빈 자리
            if count == 0:  # 필요한 만큼 빈 자리를 찾았을 때
                result[j] = i + 1  # 키가 1부터 N까지이므로 i+1로 배치
                break
            else:
                count -= 1  # 빈 자리 하나 소모

print(*result)  # 결과 출력


