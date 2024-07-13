from collections import deque

def bfs(dic, start, visited):
    q = deque([start])
    while q:
        node = q.popleft()
        if not visited[node]:
            visited[node] = True
            connected_node = dic[node]
            if not visited[connected_node]:
                q.append(connected_node)

def circle_num(lst):
    graph = {i + 1: lst[i] for i in range(len(lst))}
    visited = [False] * (len(lst) + 1)
    cycle_count = 0
    
    for i in range(1, len(lst) + 1):
        if not visited[i]:
            bfs(graph, i, visited)
            cycle_count += 1
            
    print(cycle_count)

T = int(input())

for i in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    circle_num(lst)
