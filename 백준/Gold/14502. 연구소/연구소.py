from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

virus = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]
empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

dr = [-1,1,0,0]
dc = [0,0,-1,1]


def in_range(r,c):
  return (0<=r<n and 0<=c<m)

def bfs(temp_graph):
    q = deque(virus)
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if in_range(nr, nc) and temp_graph[nr][nc] == 0:
                temp_graph[nr][nc] = 2
                q.append((nr, nc))
    return temp_graph

def count_safe(temp_graph):
    return sum(row.count(0) for row in temp_graph)


def comb(arr,n):
    result = []
    if n>len(arr):
        return result
    if n==1:
        for i in arr:
            result.append([i])
    elif n>1:
        for i in range(len(arr)- n+1):
            next_lst = comb(arr[i+1:],n-1)
            for j in next_lst:
                result.append([arr[i]] + j)
    return result

max_safe = 0
for walls in comb(empty, 3):
    temp_graph = [row[:] for row in graph]
    for r, c in walls:
        temp_graph[r][c] = 1
    spread_graph = bfs(temp_graph)
    safe = count_safe(spread_graph)
    max_safe = max(max_safe, safe)

print(max_safe)
