n,m = map(int,input().split())

def perm_rep(arr,n):
    result = []
    if n==0:
        return[[]]
    for i in range(len(arr)):
        for p in perm_rep(arr,n-1): # 나머지 중에서 n-1 뽑기
            result.append([arr[i]]+p)
    return result


lst = list(range(1, n+1))

result = perm_rep(lst,m)

for x in result:
    print(" ".join(map(str,x)))