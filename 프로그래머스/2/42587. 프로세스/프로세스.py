from collections import deque

def check_max(q):
    max_idx,max_val = 0,0
    for i,val in q:
        if val>max_val:
            max_idx,max_val = i,val
    return (max_idx,max_val)

def solution(priorities, location):
    answer = 0
    
    lst = []
    q = deque()
    max_idx,max_val = 0,0
    visited = [False]*(len(priorities))
    for i in range(len(priorities)):
        lst.append((i,priorities[i]))
        q.append((i,priorities[i]))
        if priorities[i] > max_val:
            (max_idx,max_val) = (i,priorities[i])
    # max_idx,max_val 알고있는 상태에서
    cnt=0
    while q:
        (idx,now) = q.popleft()
        if (now < max_val) and visited[max_idx] == False: #아직 실행 못시키면
            q.append((idx,now))
        else: # now >= max_val 혹은 최대 이미 방문 했다면:
            if idx == location:
                return cnt+1
            else: #최대긴 하지만 궁금한 위치는 아니라면
                cnt+=1 #프로세스 실행(q에 다시 안넣음)
                visited[idx] = True
                # max_idx,max_val = idx,now  -> 이렇게 해버리면, 이미 q에 들어간 두번째 최대값이 아니라, 내가 최대라고 인식해버림
                max_idx,max_val = check_max(q)
                
                
        
    return answer