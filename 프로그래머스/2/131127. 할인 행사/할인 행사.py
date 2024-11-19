
def solution(want, number, discount):
    
    wanted_dict = {}
    possible_day = []
    for i in range(len(want)):
        wanted_dict[want[i]] = number[i]
    
    
    max_day = len(discount)-9
    
    for i in range(max_day):
        item_dict = {}
        lst = discount[i:i+10]
        
        for item in lst :
            if item in item_dict:
                item_dict[item]+=1      
            else:
                item_dict[item] = 1
        
        isPassed = True
        for item,count in wanted_dict.items():
            if item in item_dict.keys():
                if  item_dict[item]< count: 
                    isPassed = False
                    break
            else:
                isPassed = False
                break
            
        if isPassed:
            possible_day.append(i+1)
                
    return len(possible_day)