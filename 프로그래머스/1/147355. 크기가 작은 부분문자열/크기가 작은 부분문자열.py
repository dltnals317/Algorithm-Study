def solution(t, p):
    answer = 0
    length = len(p)
    t_lst = []
    for i in range(0,len(t)-length+1):
        group = t[i:i+length]
        t_lst.append(group)
    for num in t_lst:
        if int(num) <= int(p):
            answer+=1
    return answer