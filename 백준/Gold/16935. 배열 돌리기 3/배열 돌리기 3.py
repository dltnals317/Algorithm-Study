
# 1번 연산
def top_down_reverse(arr,N,M):
    for i in range(N // 2):
        arr[i], arr[-i - 1] = arr[-i - 1], arr[i]
    return arr


# 2번 연산
def left_right_reverse(arr,N,M):
    for i in range(N):
        for j in range(M // 2):
            arr[i][j], arr[i][-j - 1] = arr[i][-j - 1], arr[i][j]
    return arr

# 3번 연산
def right_rotate(arr,N,M):
    result_lst = []
    for j in range(M):
        lst = []
        for i in range(N):
            lst.append(arr[i][j])
        lst.reverse()  
        result_lst.append(lst)
       
     # N과 M이 바뀌므로 새로운 N, M을 반환
    return result_lst, M, N
        


#4번 연산
def left_rotate(arr,N,M):
    result_lst = []
    for j in range(M-1,-1,-1):
        lst = []
        for i in range(N):
            lst.append(arr[i][j]) 
        result_lst.append(lst)
    return result_lst, M, N # N과 M이 바뀌므로 새로운 N, M을 반환
        
      
def get_sub_matrix(arr,N,M):
    # Slicing the array to get four sub-matrices
    first_matrix = [row[:M//2] for row in arr[:N//2]]  # Top-left
    second_matrix = [row[M//2:] for row in arr[:N//2]] # Top-right
    forth_matrix = [row[:M//2] for row in arr[N//2:]]  # Bottom-left
    third_matrix = [row[M//2:] for row in arr[N//2:]]  # Bottom-right
 
    sub_lst_sum = []
    sub_lst_sum.append(first_matrix)
    sub_lst_sum.append(second_matrix)
    sub_lst_sum.append(third_matrix)
    sub_lst_sum.append(forth_matrix)
    
    return sub_lst_sum
#5번 연산  
def sub_matrix_change(arr, N, M):
    # 부분 행렬을 회전시키고 다시 조합하기
    sub_lst_sum = get_sub_matrix(arr, N, M)
    # 부분 행렬 회전
    sub_lst_sum = [sub_lst_sum[3], sub_lst_sum[0], sub_lst_sum[1], sub_lst_sum[2]]

    top_left, top_right,bottom_right,bottom_left  = sub_lst_sum

    # 조합하여 전체 배열 만들기
    new_array = []
    for i in range(len(top_left)):
        new_array.append(top_left[i] + top_right[i])
    for i in range(len(bottom_left)):
        new_array.append(bottom_left[i] + bottom_right[i])
    
    return new_array

def sub_matrix_change_reverse(arr, N, M):
    # 부분 행렬을 회전시키고 다시 조합하기 (반대 방향)
    sub_lst_sum = get_sub_matrix(arr, N, M)
    # 부분 행렬 회전 (반대 방향)
    sub_lst_sum = [sub_lst_sum[1], sub_lst_sum[2], sub_lst_sum[3], sub_lst_sum[0]]

    top_left, top_right, bottom_right,bottom_left  = sub_lst_sum

    # 조합하여 전체 배열 만들기
    new_array = []
    for i in range(len(top_left)):
        new_array.append(top_left[i] + top_right[i])
    for i in range(len(bottom_left)):
        new_array.append(bottom_left[i] + bottom_right[i])
    
    return new_array

# 사용자 입력 처리
N, M, R = map(int, input().split())

array = []
for _ in range(N):
    array.append(list(map(int, input().split())))


calculate_lst = [top_down_reverse, left_right_reverse, right_rotate, left_rotate, sub_matrix_change, sub_matrix_change_reverse]

# 사용자 입력에 따라 연산 수행
cal_num_lst = list(map(int, input().split()))

result = array
for turn in cal_num_lst:
    idx = turn - 1
    if idx in [2, 3]:  # 3번과 4번 연산일 경우 N과 M이 바뀌는 경우를 처리
        result, N, M = calculate_lst[idx](result, N, M)
    else:
        result = calculate_lst[idx](result, N, M)

# 최종 배열 출력
for row in result:
    print(" ".join(map(str, row)))