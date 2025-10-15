from collections import defaultdict
def solution(participant, completion):
    answer = ''
    completion_cnt_hash = defaultdict(int)
    for name in completion:
        completion_cnt_hash[name] +=1
        
    for name in participant:
        completion_cnt_hash[name] -=1
        
    for key,value in completion_cnt_hash.items():
        if value <0:
            answer = key
            break
    return answer
    
    #시간초과
#     for name in participant:
#         if name not in completion: #완료목록에 없으면
#             return name
#         else: #완료목록에 있어도 점검 필요
#             if completion_cnt_hash[name] == 0:
#                 return name
#             else:
#                 completion_cnt_hash[name]-=1
#                 continue
                
            
    