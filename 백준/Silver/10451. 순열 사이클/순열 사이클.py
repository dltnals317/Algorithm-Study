from collections import deque

def bfs(dic, start):
    cnt = 0
    oneself = []
    visited = [False] * (len(dic) + 1)
    
    # 자기 자신을 가리키는 경우 처리
    for key, value in dic.items():
        if key == value:
            cnt += 1
            oneself.append(key)
    
    for key in oneself:
        del dic[key]
        visited[key] = True
    
    for key in dic:
        if not visited[key]:
            q = deque([key])
            while q:
                node = q.popleft()
                if not visited[node]:
                    visited[node] = True
                    connected_node = dic[node]
                    q.append(connected_node)
            cnt += 1
                
    return cnt
        
def circle_num(lst):
    graph = {idx + 1: num for idx, num in enumerate(lst)}
    result = bfs(graph, 1)
    print(result)

# 테스트 케이스 입력 받기
T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    circle_num(lst)
