# 윈도우의 최소 크기는 1, 최대 크기는 element의 갯수
# set에 저장


def solution(elements):
    result=set()
    current_sum = 0
    for window_size in range(1,len(elements)+1):
        current_sum = sum(elements[:window_size]) 
        result.add(current_sum)
        
        #맨 앞 원소가 한 칸 씩 밀릴 때 처리
        for i in range(1,len(elements)):
            current_sum = current_sum - elements[i-1] + elements[(i+window_size -1)%len(elements)]
            result.add(current_sum)
    return(len(result))
    
        
        
    
    
    
        
        
    return 
            