def solution(before, after):
    
    def find_alp_cnt(str):
        alp_dict = {}
        for i in range(len(str)):
            alp = str[i]
            if alp in alp_dict.keys():
                alp_dict[alp] = int(alp_dict[alp]) + 1
            else:
                alp_dict[alp] = 1
        return alp_dict
    
    before_cnt = find_alp_cnt(before)
    after_cnt = find_alp_cnt(after)
    
    for key,value in after_cnt.items():
        if key in before_cnt.keys():
            if before_cnt[key] == value:
                continue
            else:
                return 0
        else:
            return 0
    return 1
        
    
    