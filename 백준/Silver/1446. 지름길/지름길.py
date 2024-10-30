import heapq
N,D = map(int,input().split())

graph = [[] for _ in range(D+1)]
INF = int(1e9)


#시작점으로부터 거리
distance = [INF] * (D+1)

for i in range(D):
    graph[i].append((i+1,1))


for _ in range(N):
    start,end,length = map(int,input().split())
    if end>D:
        continue
    graph[start].append((end,length))


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        now_length,now = heapq.heappop(q)
        for connected_node_by_now,length_from_now in graph[now]:
            cost = now_length+length_from_now
            if distance[connected_node_by_now] > cost:
                distance[connected_node_by_now] = cost
                heapq.heappush(q,(cost,connected_node_by_now))
            

    

dijkstra(0)
print(distance[D])