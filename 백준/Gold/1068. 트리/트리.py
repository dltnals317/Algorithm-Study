# 리프노드 판단 함수
from collections import defaultdict
N = int(input())
parent_lst = list(map(int,input().split()))

target_node = int(input())
node_num = len(parent_lst)


graph = defaultdict(list)

for i,parent in enumerate(parent_lst):
    if parent == -1:
        continue
    else:    
        graph[parent].append(i)
        
# target_node가 부모의 자식 리스트에 있을 경우 제거
for parent in graph:
    if target_node in graph[parent]:
        graph[parent].remove(target_node)
        break
remove_node = []
def delete(node,tree):
    if node not in tree.keys():
        remove_node.append(node)
        return 
    for child_node in tree[node]:
        delete(child_node,tree)
    del tree[node]
    remove_node.append(node)


delete(target_node,graph)

cnt=0


for node in range(node_num):
    if node not in remove_node:
        if node not in graph.keys() or len(graph[node])==0:
            cnt+=1


print(cnt)