import sys
input = sys.stdin.readline
T = int(input().strip())


def binary_search(target,lst):
    cnt = 0
    left = 0
    right = len(lst) - 1
    while (left <= right):
        mid = (left + right) // 2
        if lst[mid] < target:
            cnt = mid+1
            left = mid + 1
        else:
            right = mid - 1
    return cnt
       
    
for _ in range(T):
    N,M = map(int,input().split())
    A_lst = [int(x) for x in input().split()]
    B_lst = [int(x) for x in input().split()]
    count = 0
    B_lst.sort()
    for x in A_lst:
        value = binary_search(x,B_lst)
        count += value
    print(count)