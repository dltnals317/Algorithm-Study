# 확정된 키 6개는 left_lst,right_lst에 담아둔다
# 4가지 키 (left_lst에도 right_lst에도 없는 키)의 경우, 현재 left와 right와의 거리를 측정한다
# 거리가 같다면, hand를 기반으로 한다


def solution(numbers, hand):
    left_lst = [1,4,7]
    right_lst = [3,6,9]
    length_dict = {
        1:[0,0],
        2:[0,1],
        3:[0,2],
        4:[1,0],
        5:[1,1],
        6:[1,2],
        7:[2,0],
        8:[2,1],
        9:[2,2],
        0:[3,1],
        '*': [3, 0],
        '#': [3, 2]
    }
    left = '*'
    right = '#'
    result_lst = []
    for num in numbers:
        if num in left_lst:
            result_lst.append('L')
            left = num
        elif num in right_lst:
            result_lst.append('R')
            right = num
            
        else: #2,5,8,0
            from_left = abs(length_dict[left][0] - length_dict[num][0]) + abs(length_dict[left][1] - length_dict[num][1])
            from_right = abs(length_dict[right][0] - length_dict[num][0]) + abs(length_dict[right][1] - length_dict[num][1])
            
            if from_left > from_right:
                result_lst.append('R')
                right = num
            elif from_left < from_right:
                result_lst.append('L')
                left = num
            else:
                if hand == "left":
                    result_lst.append('L')
                    left = num
                elif hand == "right":
                    result_lst.append('R')
                    right = num
    answer = "".join(result_lst)
                    
                
        
    return answer