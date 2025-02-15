from collections import deque
def solution(arr):
    answer = []
    
    for x in arr: #1,1,3,3,0,1,1
        if len(answer)==0:
            answer.append(x)
        else:
            k = answer[-1]
            if x == k:
                continue
            else:
                answer.append(x)
    
        
    return answer