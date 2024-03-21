import sys
input = sys.stdin.readline
n = int(input())
a_graph = []
b_graph = []

for i in range(n):
    lst = list(map(int,input().split()))
    a_graph.append(lst)


for i in range(n):
    lst = list(map(int,input().split()))
    b_graph.append(lst)

def devide_lst(lst):
    result_lst = []
    for i in range(n-1, -1, -1): #2,1,0
        tmp_lst = lst[0:i+1]
        result_lst.append(tmp_lst)
        lst = lst[i+1:]
   
    return result_lst

def minus(graph):
    graph_copy = [row[:] for row in graph]  # 깊은 복사 수행
    total_lst = []
    for i in range(len(graph_copy)):
        tmp_lst = []
        for lst in graph_copy[i:]:
            tmp_lst.append(lst[i])
        total_lst.append(tmp_lst)
    result = []
    for lst in total_lst[::-1]:
        result.append(lst)
    return result

def plus(graph):
    graph_copy = [row[:] for row in graph]  # 깊은 복사 수행
    total_lst = []
    reset_lst = []
    for i in range(len(graph_copy)):
        tmp_lst = []
        for lst in graph_copy[::-1]:
            tmp_lst.append(lst)
    while tmp_lst:
        for lst in tmp_lst:
            if len(lst) == 0:
                tmp_lst.remove(lst)
            else:
                value = lst.pop()
                reset_lst.append(value)
    result = devide_lst(reset_lst)
    final_lst = []
    for i in range(len(result)):
        final_lst.append(result[-i - 1])
    return final_lst

def symmetry_func(lst):
    lst_copy = [row[:] for row in lst]  # 깊은 복사 수행
    for each in lst_copy:
        for i in range(len(each)//2):
            tmp = each[i]
            each[i] = each[-i-1]
            each[-i-1] = tmp
    return lst_copy

def minimum_diff(original,sym,sym_minus,sym_plus,minus,plus,b):
    cnt_original = 0
    cnt_sym = 0
    cnt_sym_minus = 0
    cnt_sym_plus = 0
    cnt_minus = 0
    cnt_plus = 0
    
    for idx,lst in enumerate(original):
        if lst == b[idx]:
            continue
        else:
            for i,num in enumerate(lst):
                if num == b[idx][i]:
                    continue
                else:
                    cnt_original+=1
    for idx,lst in enumerate(sym):
        if lst == b[idx]:
            continue
        else:
            for i,num in enumerate(lst):
                if num == b[idx][i]:
                    continue
                else:
                    cnt_sym+=1
    for idx,lst in enumerate(sym_minus):
        if lst == b[idx]:
            continue
        else:
            for i,num in enumerate(lst):
                if num == b[idx][i]:
                    continue
                else:
                    cnt_sym_minus+=1
    for idx,lst in enumerate(sym_plus):
        if lst == b[idx]:
            continue
        else:
            for i,num in enumerate(lst):
                if num == b[idx][i]:
                    continue
                else:
                    cnt_sym_plus+=1
    for idx,lst in enumerate(minus):
        if lst == b[idx]:
            continue
        else:
            for i,num in enumerate(lst):
                if num == b[idx][i]:
                    continue
                else:
                    cnt_minus+=1      
    for idx,lst in enumerate(plus):
        if lst == b[idx]:
            continue
        else:
            for i,num in enumerate(lst):
                if num == b[idx][i]:
                    continue
                else:
                    cnt_plus+=1   
                    
    min_diff = min(cnt_original, cnt_sym, cnt_sym_minus, cnt_sym_plus, cnt_minus, cnt_plus)
    return min_diff
        
    

only_sym = symmetry_func(a_graph)

minus_result = minus(a_graph)  # 함수를 호출하여 반환된 결과를 변수에 저장

minus_symmetry = symmetry_func(minus_result)  # 함수를 호출하여 반환된 결과를 변수에 저장

plus_result = plus(a_graph)  # 함수를 호출하여 반환된 결과를 변수에 저장

plus_symmetry = symmetry_func(plus_result)  # 함수를 호출하여 반환된 결과를 변수에 저장

result = minimum_diff(a_graph,only_sym,minus_symmetry,plus_symmetry,minus_result,plus_result,b_graph)
print(result)
