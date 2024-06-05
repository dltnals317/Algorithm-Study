#4묶음씩 루프를 돌면서, 4개가 같은거 있다면 x로 바꾸기(지울거니까)


def solution(m, n, board):
    answer=0
    for i in range(m):
        board[i] = list(board[i])
    
    def search():
        del_index_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if (board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]) and board[i][j]!=0:
                    del_index_set.add((i,j))
                    del_index_set.add((i,j+1))
                    del_index_set.add((i+1,j))
                    del_index_set.add((i+1,j+1))
        return del_index_set
    
    def delete(lst):
        for tup in lst:
            board[tup[0]][tup[1]] = 0
    
    def pulling():
        for i in range(m-1,-1,-1): #m-1 idx부터 0 idx까지 내림차순
            for j in range(n):
                if board[i][j] == 0:
                    for k in range(i-1,-1,-1):
                        if board[k][j] !=0:
                            board[i][j] = board[k][j]
                            board[k][j] = 0
                            break
                            
    while True:
        delete_block = list(search())
        if len(delete_block) == 0: #가 비어있으면(루프를 돌다가, 4개가 같은게 존재하지 않으면)
            break
        answer += len(delete_block)
        delete(delete_block)
        pulling()
            
    return answer