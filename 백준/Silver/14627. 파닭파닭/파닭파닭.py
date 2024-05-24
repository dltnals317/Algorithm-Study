import sys
input = sys.stdin.readline

s, c = map(int, input().split())
l_lst = []

for _ in range(s):
    L = int(input())
    l_lst.append(L)

left = 1
right = max(l_lst)
while left <= right:
    mid = (left + right) // 2
    lst = [x // mid for x in l_lst]
    if sum(lst) < c:
        right = mid - 1
    else:
        left = mid + 1

max_length = right
used_lst = [(l_lst[i] // max_length) * max_length for i in range(len(l_lst))]
remain_lst = sum(l_lst) - (max_length * c)
print(remain_lst)
