from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
distance = [0] * (n + 1)

for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)


def bfs_family(start, target):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        if current == target:
            return distance[current]
        else:
            for connected_one in graph[current]:
                if visited[connected_one] == False:
                    queue.append(connected_one)
                    visited[connected_one] = True
                    distance[connected_one] += distance[current]+ 1


    return -1


cnt = bfs_family(a, b)

print(cnt)