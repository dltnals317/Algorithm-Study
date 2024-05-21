#앞 두개는 X길이를 보고
#뒤 두개는 Y길이를 보면 되겠다

def solution(dots):
    answer = 0
    w_lst = []
    h_lst = []
    for dot in dots:
        if dot[0] not in w_lst:
            w_lst.append(dot[0])
        if dot[1] not in h_lst:
            h_lst.append(dot[1])
    w2,w1 = max(w_lst),min(w_lst)
    h2,h1 = max(h_lst),min(h_lst)

    w3 = w2 - w1
    h3 = h2 - h1
    
    answer = w3 * h3
    return answer