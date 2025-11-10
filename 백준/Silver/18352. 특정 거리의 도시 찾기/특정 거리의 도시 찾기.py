import sys
from collections import deque, defaultdict

input = sys.stdin.readline  

n, m, k, x = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n + 1)
visited[x] = True

q = deque([(x, 0)])
result = []

while q:
    node, dist = q.popleft()

    if dist == k:
        result.append(node)
        continue

  
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            q.append((next_node, dist + 1))


if result:
    result.sort()
    sys.stdout.write("\n".join(map(str, result)) + "\n") 
else:
    sys.stdout.write("-1\n")
