import sys
input = sys.stdin.readline
from collections import deque

def connect_stone(lst, start, n):
    visited_queue_idx = deque()
    visited_set = set()
    visited_queue_idx.append(start - 1)
    visited_set.add(start)
    
    while visited_queue_idx:
        node_idx = visited_queue_idx.popleft()
        distance = lst[node_idx]
        if node_idx - distance >=0 and node_idx - distance + 1 not in visited_set:
            visited_queue_idx.append(node_idx - distance)
            visited_set.add(node_idx - distance + 1)
        if node_idx + distance < n and node_idx + distance + 1 not in visited_set:
            visited_queue_idx.append(node_idx + distance)
            visited_set.add(node_idx + distance + 1)
                
    return visited_set

n = int(input())
graph = list(map(int, input().split()))
s = int(input())

test = connect_stone(graph, s, n)

print(len(test))