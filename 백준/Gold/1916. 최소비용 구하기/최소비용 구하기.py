import heapq
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    start,end,cost = map(int,input().split())
    graph[start].append((end,cost))

def min_cost_heapq(start):
    INF = int(1e9)
    distance = [INF] * (n+1)
    cost_que = []
    heapq.heappush(cost_que,(0,start))
    distance[start] = 0
    while cost_que:
        length,now = heapq.heappop(cost_que)
        if distance[now] < length:
            continue

        for destination,dist in graph[now]:
            if distance[now] + dist < distance[destination]:
                distance[destination] = distance[now] + dist
                heapq.heappush(cost_que,(distance[destination],destination))
    return distance      
        
            
            
                
start_city,end_city = map(int,input().split())

distance_lst=[]
distance_lst = min_cost_heapq(start_city)
print(distance_lst[end_city])