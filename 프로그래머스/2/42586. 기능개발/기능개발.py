from collections import deque
def solution(progresses, speeds):
    answer = []
    q = deque()
    tmp_stack = []
    for i in range(len(progresses)):
        remain_process = 100 - progresses[i]
        days = (remain_process // speeds[i]) + (0 if remain_process % speeds[i] == 0 else 1)
        q.append(days)
    
    start = q[0]
    tmp = []
    cnt = 0
    
    while q:
        print("q",q)
        print("tmp",tmp)
        print("start",start)
        target = q.popleft()
        if target <= start:
            tmp.append(target)
        else:
            answer.append(len(tmp))
            start = target
            tmp = [target]
           
    if len(tmp)>0:
        answer.append(len(tmp))
    return answer