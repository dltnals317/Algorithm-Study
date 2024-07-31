import sys
import heapq

input = sys.stdin.readline
beer = []
N,M,K = map(int,input().split())
for i in range(K):
    v,c = map(int,input().rstrip().split())
    beer.append([v,c])

beer.sort(key = lambda x : x[1]) #도수를 기준으로 오름차순 정렬

heap = []
total_preference = 0
gan = -1
for v,c in beer: #beer은 도수를 기준으로 정렬되어있음(선호도x)
    heapq.heappush(heap,v) #힙에 맥주의 선호도 추가(나중에 작은 선호도 기준으로 빼기위해)
    total_preference+=v

    if len(heap) > N: #먹을 수 있는 맥주 양 초과하면
        total_preference -= heapq.heappop(heap) #선호도 작은 순으로 빼기
    if len(heap)==N and total_preference >=M:
        gan = c
        break
        

print(gan)
            
    
    
        