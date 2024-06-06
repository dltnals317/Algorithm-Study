import sys
input = sys.stdin.readline
N,M = map(int,input().split())
inverse = []
for i in range(M):
    a,b = map(int,input().split())
    inverse.append((a,b))

lst = []
for i in range(N+1):
    lst.append(i)

for tup in inverse:
    start,end = tup[0],tup[1]
    x = (end+1 - start) // 2
    for i in range(x): 
        lst[start+i] , lst[-i+end] =  lst[-i+end] , lst[start+i]
lst = lst[1:]
lst = list(map(str,lst))
print(' '.join(lst))
        