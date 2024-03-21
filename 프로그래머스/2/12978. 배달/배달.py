import heapq

def solution(N, road, K):
    answer = 0
    q = []
    INF = int(1e9)
    distance = [INF] * (N+1) #시작도시(1번도시)부터 index까지 거리->처음엔 무한대로 초기화
    graph = [[] for _ in range(N+1)]
    
    for lst in road:
        start,end,length = lst[0],lst[1],lst[2]
        graph[start].append((end,length))
        graph[end].append((start,length))
    
    heapq.heappush(q,(0,1)) #1번도시부터 시작, 1번도시에서 1번도시는 거리가 0
    distance[1] = 0
    while q:
        dist_from_one_to_now,now = heapq.heappop(q)
        if distance[now] < dist_from_one_to_now:
            continue
        else:
            distance[now] = dist_from_one_to_now
            
            
        for end,length in graph[now]:
            cost = dist_from_one_to_now + length
            if cost < distance[end]:
                distance[end] = cost
                heapq.heappush(q,(cost,end))
    print(distance)        
    for dist in distance:
        if dist > K:
            continue
        else: #K보다 적게걸릴 조건 만족하는 경우
            answer +=1
    print(answer)            

    return answer