import sys
input = sys.stdin.readline

def binary_search(target, lst):
    cnt = 0
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] < target:
            cnt = mid + 1  # mid를 기준으로 그보다 작은 값의 개수는 mid + 1개
            left = mid + 1
        else:
            right = mid - 1
    return cnt

T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().split())
    A_lst = [int(x) for x in input().split()]
    B_lst = [int(x) for x in input().split()]
    B_lst.sort()
    count = 0
    for x in A_lst:
        value = binary_search(x, B_lst)
        count += value
    print(count)
