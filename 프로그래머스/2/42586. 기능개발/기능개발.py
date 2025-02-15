from collections import deque
def solution(progresses, speeds):
    answer = []
    
    #필요한 작업 기간 기준으로 스택/큐에 넣기
    
    q = deque()
    
    for i,pg in enumerate(progresses):
        remain_pg = 100 - pg
        need_time = remain_pg // speeds[i]
        if (remain_pg % speeds[i] == 0):
            q.append(need_time)
        else:
            q.append(need_time+1)
    cnt = 1
    pivot = q.popleft()
    while q:
        #[5,10,1,1,20,1]
        
        now = q.popleft()
        
        if(pivot >= now):
            cnt+=1
            
        else:
            answer.append(cnt)
            cnt = 1
            pivot = now
    answer.append(cnt)
            
    return answer