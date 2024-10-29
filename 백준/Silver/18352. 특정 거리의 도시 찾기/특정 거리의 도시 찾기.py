import heapq
import sys
input = sys.stdin.readline
N,M,K,X = map(int,input().split())

graph = [[] for _ in range(N+1)]

INF = int(1e9)
distance_lst = [INF] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append((b,1))

def priory_distance():
    q = []
    heapq.heappush(q,(0,X)) # q = [(0,X)]
    distance_lst[X] = 0
    while q:
        distance,now = heapq.heappop(q) #0,X
        for city,length in graph[now]: #(2,1),(3,1):
            if (distance_lst[now]+ 1 <distance_lst[city]):
                distance_lst[city] = distance_lst[now] + 1
                heapq.heappush(q,(distance_lst[city],city))
            
    return distance_lst
                
            
lst = priory_distance()
okay=[]
for i in range(len(lst)):
    if lst[i] == K:
        okay.append(i)
if len(okay)== 0:
    print(-1)
else:
    print(*okay)
        