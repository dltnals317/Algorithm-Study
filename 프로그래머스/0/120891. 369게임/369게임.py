def solution(order):
    answer = 0
    str_num = str(order)
    for x in str_num:
        print(x)
        if x == '3' or x == '6' or x == '9':
            answer +=1
    return answer