from collections import deque

# 풍선의 개수 입력
N = int(input())

# 풍선의 값 입력
balloons = list(map(int, input().split()))

# 풍선의 인덱스와 값을 쌍으로 저장
d = deque(enumerate(balloons))

# 풍선을 터뜨리는 순서 저장
result = []

# 첫 번째 풍선부터 터뜨리기 시작
while d:
    # 현재 터뜨릴 풍선의 인덱스와 값
    idx, value = d.popleft()
    # 터뜨린 풍선의 인덱스를 기록 (1-based)
    result.append(idx + 1)
    
    # 풍선이 모두 터졌으면 종료
    if not d:
        break
    
    # 풍선의 값에 따라 이동
    if value > 0:
        # 오른쪽으로 (value - 1)만큼 회전
        d.rotate(-(value - 1))
    else:
        # 왼쪽으로 -value만큼 회전
        d.rotate(-value)

# 결과 출력
print(*result)