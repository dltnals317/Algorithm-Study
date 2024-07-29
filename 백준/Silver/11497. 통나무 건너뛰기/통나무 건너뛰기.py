#증가하다가 감소하는 형태여야함
T = int(input())
for i in range(T):
    N = int(input())
    lst = list(map(int,input().split()))
    tmp = [0]* len(lst)
    lst.sort()
    for i in range(0,(len(lst)//2),1):
        left,right = 2*i,2*i+1
        tmp[i],tmp[-1-i] = lst[left],lst[right]
       
    tmp[len(lst)//2] = lst[-1]

    result = []
    for i in range(len(tmp)):
        val =  abs(tmp[i]-tmp[(i+1)%len(tmp)])
        result.append(val)
    print(max(result))
