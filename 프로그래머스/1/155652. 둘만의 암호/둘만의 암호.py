def solution(s, skip, index):
    alpha_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for ch in skip:
        alpha_lst.remove(ch)
    
    answer = ''
    
    s_list = list(s)
    for i,ch in enumerate(s_list):
        idx = (alpha_lst.index(ch))
        change_idx = (idx+index) % len(alpha_lst)
        change_value = alpha_lst[change_idx]
        s_list[i] = change_value
        
    
    return ''.join(s_list)