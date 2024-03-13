import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
n,d = map(int,input().split())
graph = [[] for _ in range (d+1)] 
distance = [INF] * (d+1)

for i in range(d):
    graph[i].append((i+1, 1)) #모든 거리

for _ in range(n):
    s, e, l = map(int, input().split())
    if e > d :
        continue
    graph[s].append((e,l))
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        for node,length in graph[now]:
            cost = dist + length
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q,(cost, node))
                 
dijkstra(0)
print(distance[d])    