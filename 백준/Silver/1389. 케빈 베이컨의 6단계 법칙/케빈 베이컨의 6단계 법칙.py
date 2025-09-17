from collections import defaultdict
n,m = map(int,input().split())


friend_graph = [[1000]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    friend_graph[a][b] = 1
    friend_graph[b][a] = 1
for node in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            friend_graph[a][b] = min(friend_graph[a][b],friend_graph[a][node] + friend_graph[node][b])

result = 0
min_count =1e9

for i in range(len(friend_graph)):
    if sum(friend_graph[i]) < min_count:
        min_count = sum(friend_graph[i])
        result = i

print(result)        
    