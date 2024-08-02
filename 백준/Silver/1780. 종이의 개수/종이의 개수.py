N = int(input())

entire = []
for i in range(N):
    lst = list(map(int,input().split()))
    entire.append(lst)

def all_zero(two_matraix):
    for row in two_matraix:
        for element in row:
            if element != 0:
                return False
    return True

def all_one(two_matraix):
    for row in two_matraix:
        for element in row:
            if element != 1:
                return False
    return True

def all_minus(two_matraix):
    for row in two_matraix:
        for element in row:
            if element != -1:
                return False
    return True


def get_submatrix(arr,N):
    matrix = []
    size = N//3
    for i in range(0,len(arr),size):
        for j in range(0,len(arr[i]),size):
            submatrix = [row[j:j+size] for row in arr[i:i+size]]
            matrix.append(submatrix)
    return matrix    

def count_paper(two_matrix_arr,N):
    if all_zero(two_matrix_arr):
        return (0, 1, 0)
    elif all_one(two_matrix_arr):
        return (0, 0, 1)
    elif all_minus(two_matrix_arr):
        return (1, 0, 0)
   
    else:
        zero, one, minus = 0, 0, 0
        sub_matrices = get_submatrix(two_matrix_arr, N)
        for lst in sub_matrices:
            m,z,o = count_paper(lst,N//3)
            zero+=z
            one+=o
            minus+=m
    return (minus,zero,one)            
    
    

result = count_paper(entire,N)
for x in result:
    print(x)
