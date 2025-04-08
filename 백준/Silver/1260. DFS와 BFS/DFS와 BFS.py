import sys
input = sys.stdin.readline
from collections import deque 
n,m,v = map(int,input().split())


graph = [[] for _ in range(n+1)]
for i in range(m):
    node,connected_node = map(int,input().split())
    graph[node].append(connected_node)
    graph[connected_node].append(node)
    

def dfs(graph,node,visited): #재귀
    visited[node] = True
    print(node,end= " ")
    for i in sorted(graph[node]):
        if not visited[i]:
            dfs(graph,i,visited)


                
def bfs(graph,node,visited): #큐
    queue = deque([node])
    visited[node] = True
    while queue: #큐가 비어있지 않을 때까지 반복
        out_node = queue.popleft() #꺼내고 나서
        print(out_node,end=" ")
        for i in sorted(graph[out_node]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    

visited = [False]*(n+1)
dfs(graph,v,visited)
print()
visited = [False]*(n+1)
bfs(graph,v,visited)