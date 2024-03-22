import sys
input = sys.stdin.readline
n = int(input())
INF = int(1e9)
graph = []

#그래프 채우기
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)


for k in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][b] > 0:
                continue
            else: #graph[a][b] == 0 a에서 b로 가는 경로 없으면
                if graph[a][k] !=0 and graph[k][b]!=0:
                    graph[a][b] = 1
                else:
                    continue
                
for row in graph:
    print(' '.join(map(str, row)))