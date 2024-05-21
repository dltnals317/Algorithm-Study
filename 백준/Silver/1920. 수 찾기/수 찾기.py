import sys
input = sys.stdin.readline
N = int(input().strip())
A_lst = [int(x) for x in input().split()]

M = int(input().strip())
B_lst = [int(x) for x in input().split()]

def binary_search(target,lst):
    left_idx = 0
    right_idx = len(lst)-1
    while (left_idx <= right_idx):
        mid = (left_idx + right_idx) // 2
        if target > A_lst[mid]:
            left_idx = mid+1 
        elif target < A_lst[mid]:
            right_idx = mid-1
        elif target == A_lst[mid]:
            return 1
    return 0        
        


A_lst.sort()
for x in B_lst:
    value = binary_search(x,A_lst)
    print(value)