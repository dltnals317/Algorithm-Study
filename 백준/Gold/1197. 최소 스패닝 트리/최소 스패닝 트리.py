import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
v,e = map(int,input().split())


edges = []
parents = {}


for i in range(1, v+1):
    parents[i] = i
for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))
    

def find(x):
    if parents[x] !=x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[y] = x

edges.sort()

total_cost = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total_cost += cost

print(total_cost)