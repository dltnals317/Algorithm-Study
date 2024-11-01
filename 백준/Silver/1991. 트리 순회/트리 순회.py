import sys
input = sys.stdin.readline
N = int(input())


def preorder(now,order_table):#전위순회
    if now == ".":
        return
    order_table.append(now)
    left_ch,right_ch = node_graph[now]
    preorder(left_ch,order_table)
    preorder(right_ch,order_table)
   
    return order_table
    
def inorder(now,order_table): #중위순회
    if now == ".":
        return
    left_ch,right_ch = node_graph[now]
    inorder(left_ch,order_table)
    order_table.append(now)
    inorder(right_ch,order_table)

    return order_table
    
    
   
def postorder(now,order_table): #후위순회
    if now == ".":
        return
    left_ch,right_ch = node_graph[now]
    postorder(left_ch,order_table)
    postorder(right_ch,order_table)
    order_table.append(now)

    return order_table

node_graph = {}
for _ in range(N):
    parent,left_child,right_child = input().split()
    node_graph[parent] = [left_child,right_child]
    

preorder_table = preorder('A',[])
inorder_table = inorder('A',[])
postorder_table = postorder('A',[])

print("".join(preorder_table))
print("".join(inorder_table))
print("".join(postorder_table))