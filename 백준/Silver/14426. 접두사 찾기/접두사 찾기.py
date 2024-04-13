import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self,key,data=None):
        self.key = key
        #self.data = data
        self.children = {}

class Tries:
    def __init__(self):
        self.head = Node(None)
    def insert(self,string):
        current_node = self.head
        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
           
    def starts_with(self,prefix):
        current_node = self.head
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return 0
        return 1
                
            

def count_prefix():
    n,m = map(int,input().split())
    trie = Tries()
    for _ in range(n):
        trie.insert(input().rstrip())
    cnt = 0
    for _ in range(m):
        cnt+=trie.starts_with(input().rstrip())
    return cnt    
    

test = count_prefix()
print(test)