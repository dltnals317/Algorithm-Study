from collections import deque,defaultdict
import sys

input = sys.stdin.readline
n,m,k,x = map(int,input().split())



graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
visited = [False]*(n+1)


q = deque([(x,0)])
visited[x] = True
result = []


while(q):
    node, dist = q.popleft()
    if dist == k:
        result.append(node)
        continue
    if dist < k:
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, dist + 1))
if result:
    result.sort()
    for r in result:
        print(r)
else:
    print(-1)
        