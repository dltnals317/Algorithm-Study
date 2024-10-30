lst = []
num=1
while len(lst)<1000:
    for _ in range(num):
        lst.append(num)
    num+=1

A,B = map(int,input().split())
result = 0
for i in range(A-1,B):
    result+=lst[i]
    
print(result)
  