import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
input_lst = deque()

total=0

for _ in range(N):
    value = list(map(int, input().rstrip().split()))
    input_lst.append(value)

for _ in range(N):
    now = input_lst.popleft()
    if now[0] == 1: #과제를 뽑은 경우
        now[-1]-=1 #과제 시간 1개 빼고
        if now[-1] == 0:
            total+= now[-2]
        else:
            input_lst.append(now) #다시 뒤에 넣어주기
    elif now[0] == 0:
        tmp = input_lst.pop()
        if len(tmp) > 0:
            tmp[-1]-=1
            if tmp[-1] == 0:
                total+=tmp[-2]
            else:
                input_lst.append(tmp)
        else:
            continue
print(total)