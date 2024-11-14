import heapq

def solution(scoville, K):
    # 힙을 만든다
    heap = []
    for flavor in scoville:
        heapq.heappush(heap, flavor)  # 가장 작은 값이 항상 heap의 루트가 된다.
    
    cnt = 0  # 연산 횟수 초기화
    
    # 힙에 값이 두 개 이상일 때만 반복
    while len(heap) > 1:
        lowest = heapq.heappop(heap)  # 가장 작은 값
        low = heapq.heappop(heap)     # 두 번째로 작은 값
        
        if lowest >= K:  # 이미 가장 작은 값이 K 이상이라면 더 이상 연산할 필요가 없다
            heapq.heappush(heap, low)  # 다시 넣어줌
            break
        
        # 새로운 음식의 스코빌 지수 계산
        total_scoville = lowest + (low * 2)
        heapq.heappush(heap, total_scoville)  # 새로운 음식은 힙에 추가
        
        cnt += 1  # 연산 횟수 증가
    
    # 만약 heap에 하나만 남고, 그 값이 K 미만이라면 실패
    if heap and heap[0] >= K:
        return cnt
    return -1
