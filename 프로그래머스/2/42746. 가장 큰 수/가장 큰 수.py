def solution(numbers):
    num_dict = {}
    result_lst = []
    for num in numbers:
        front = str(num)[0]
        if front in num_dict.keys():
            num_dict[front].append(num)
        else:
            num_dict[front] = [num]
   
    print(num_dict)    
        
    answer = ''
    return answer


# 무조건 앞자리가 큰게 오면 좋은 것?
# 1자리수는 쉬운데, 2자리로 넘어갈 경우....
#각 숫자를 dic으로 관리?
