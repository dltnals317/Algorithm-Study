# def danger_write(board):
#         for i in range(1,len(board)-1):
#             row_lst = board[i]
#             for j in range(1,len(row_lst)-1): #모서리 제외하고 j=1,2,3
#                 if board[i][j] == 1:
#                     print("i",i)
#                     print("j",j)
#                     board[i-1][j-1] = 1
#                     board[i-1][j]= 1
#                     board[i-1][j+1] = 1
#                     board[i][j-1] = 1
#                     board[i][j+1] = 1
#                     board[i+1][j-1] = 1
#                     board[i+1][j] = 1
#                     board[i+1][j+1] = 1
#         return board  
def solution(board):   
    dx = [-1,0,1]
    dy = [-1,0,1]
    size = len(board)
    bomb = []
    for i in range(size): # i =0,1,2,3,4
        for j in range(size): #j =0,1,2,3,4
            if board[i][j] == 1:
                bomb.append((i,j))
    for x,y in bomb:
        for i in dx:
            for j in dy:
                nx = x + i
                ny = y + j
                if 0 <= nx < size and 0 <= ny < size:  # Check if within bounds
                    board[nx][ny] = 1
                
    result = 0
    for lst in board:
        for value in lst:
            if value == 0:
                result+=1
    
    return result