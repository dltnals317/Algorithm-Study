def permutations(n_arr, m):
    n_arr.sort()  # 사전순 정렬
    result = []
    is_used = [False] * len(n_arr)

    def backtracking(tmp_permutation_lst):
        if len(tmp_permutation_lst) == m:
            result.append(tmp_permutation_lst[:])
            return
        
        prev_num = None
        for i in range(len(n_arr)):
            if not is_used[i] and n_arr[i] != prev_num:
                is_used[i] = True
                tmp_permutation_lst.append(n_arr[i])
                backtracking(tmp_permutation_lst)
                tmp_permutation_lst.pop()
                is_used[i] = False
                prev_num = n_arr[i]
    
    backtracking([])
    return result


N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = permutations(arr, M)
for seq in answer:
    print(*seq)
