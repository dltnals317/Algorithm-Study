# union에서 rank 비교하는 로직도 필요

t = int(input())

    
def find(x): #루트 찾기
    if parents[x] !=x :
        parents[x] = find(parents[x])
    return parents[x]
    


def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra !=rb:
        parents[rb] = ra
        counts[ra] += counts[rb]
    return counts[ra]

        
for _ in range(t):
    parents = {}
    counts = {}
    f = int(input())
    for _ in range(f):
        a,b = input().split()
        if a not in parents:
            parents[a] = a
            counts[a] = 1
        if b not in parents:
            parents[b] = b
            counts[b] = 1    
       
        union(a, b)
        root = find(a)
        print(counts[root])
