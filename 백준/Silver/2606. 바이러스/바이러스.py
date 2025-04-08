import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n+1)
def dfs_virus(graph,node,visited):
    visited[node] = True
    for i in sorted(graph[node]):
        if visited[i] == False:
            dfs_virus(graph,i,visited)
    return visited
        

cnt = 0
visited_lst = dfs_virus(graph,1,visited)    
for x in visited_lst[2:]:
    if x == True:
        cnt+=1

print(cnt)
        