def min_chocolate_splits(K):
    # 최소 초콜릿 크기 찾기
    size = 1
    while size < K:
        size *= 2
    
    # 최소 쪼갬 횟수 계산
    remaining = K
    splits = 0
    current_piece = size
    
    while remaining > 0:
        if current_piece > remaining:
            current_piece //= 2
            splits += 1
        else:
            remaining -= current_piece
    
    return size, splits

# 입력 받기
K = int(input())

# 함수 호출 및 결과 출력
size, splits = min_chocolate_splits(K)
print(size, splits)
