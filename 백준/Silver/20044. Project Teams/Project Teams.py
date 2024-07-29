n = int(input())
lst = list(map(int,input().split()))
a = sorted(lst)
b = sorted(lst, reverse=True)

arr= []
for i in range(len(lst)):
    x = a[i]+b[i]
    arr.append(x)

print(min(arr))