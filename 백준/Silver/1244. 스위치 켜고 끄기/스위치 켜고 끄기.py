def boy_switch(num,switch_lst):
    reverse_idx = []
    for i in range(num,len(switch_lst)):
        if i%num == 0:
            reverse_idx.append(i)

    # 해당 인덱스의 스위치 상태를 반전
    for idx in reverse_idx:
        if switch_lst[idx] == 0:
            switch_lst[idx] = 1
        else:
            switch_lst[idx] = 0

    return switch_lst

def girl_switch(num,switch_lst):
    reverse_idx = [num]
    for i in range(1,len(switch_lst)):
        left_idx = num-i
        right_idx = num + i
        if 1<=left_idx and right_idx <len(switch_lst) and switch_lst[left_idx] == switch_lst[right_idx]:
            reverse_idx.append(left_idx)
            reverse_idx.append(right_idx)
        else:
            break
    # 대칭 범위에 있는 스위치 상태 반전
    for idx in reverse_idx:
        if switch_lst[idx] == 0:
            switch_lst[idx] = 1
        else:
            switch_lst[idx] = 0

    return switch_lst
    
        
    
n = int(input())
switch_lst = [0] # 첫 번째 인덱스를 무시하기 위해 0 추가
lst = list(map(int,input().split()))
for num in lst:
    switch_lst.append(num)
    
student_num = int(input())

for _ in range(student_num):
    gender,number = map(int,input().split())
    if gender == 1:
        switch_lst = boy_switch(number,switch_lst)
    else:
        switch_lst = girl_switch(number,switch_lst)

switch_lst = switch_lst[1:]
for i in range(0, len(switch_lst), 20):
    print(' '.join(map(str, switch_lst[i:i + 20])))
        