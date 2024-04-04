import sys
input = sys.stdin.readline
def preorder(tree,node,lst):
    if node == ".":
        return
    lst.append(node)
    left_child,right_child = tree[node]
    preorder(tree,left_child,lst)
    preorder(tree,right_child,lst)

    return lst
def inorder(tree,node,lst):
    if node == "." :
        return
    left_child,right_child = tree[node]
    inorder(tree,left_child,lst)
    lst.append(node)
    inorder(tree,right_child,lst)
    return lst
def postorder(tree,node,lst):
    if node == ".":
        return
    left_child,right_child = tree[node]
    postorder(tree,left_child,lst)
    postorder(tree,right_child,lst)
    lst.append(node)
    return lst
graph = {}
N = int(input())
for _ in range(N):
    parent,left_child,right_child = input().split()
    graph[parent] = [left_child,right_child]

root_node = list(graph.keys())[0]
a = preorder(graph,root_node,[])
b =inorder(graph,root_node,[])
c = postorder(graph,root_node,[])


print("".join(a))
print("".join(b))
print("".join(c))