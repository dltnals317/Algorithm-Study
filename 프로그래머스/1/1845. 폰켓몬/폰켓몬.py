def solution(nums):
    answer = 0
    selected_type = []
    hs = {}
    pocketmon_num = len(nums)//2
    #가져갈 수 있는 포켓몬 종류의 최솟값 : 1(모두 같은 종류일때), 최댓값: N/2 (가져갈 수 있는 포켓몬의 수)
    type_num = 0
    get_num = 0
    for mon in nums:
        if mon in hs:
            hs[mon] +=1
        else:
            hs[mon] = 1
    while get_num < pocketmon_num:
        for t in hs.keys():
            if get_num == pocketmon_num:
                break
            else:
                if hs[t] >0:
                    if t not in selected_type:
                        type_num+=1
                        selected_type.append(t)
                    get_num+=1
                    hs[t]-=1
                else:
                    continue
                
            
    
    return type_num