from copy import deepcopy
N = int(input())

candy_map = []
for _ in range(N):
    row = list(input())
    candy_map.append(row)




def search(two_arr):
    max_cnt = 0

    #가로 탐색
    for i in range(N): #i=0,1,2
        count = 1
        for j in range(1,N): #j=1,2
            now = two_arr[i][j]
            if two_arr[i][j] == two_arr[i][j-1]: #전것과 같다면
                count+=1
            else: #다르다면
                max_cnt = max(max_cnt,count)
                count = 1
        max_cnt = max(max_cnt,count)
    #세로 탐색
    for j in range(N):
        count = 1
        for i in range(1,N):
            now = two_arr[i][j]
            if two_arr[i][j] == two_arr[i-1][j]:
                count+=1
            else:
                max_cnt = max(max_cnt,count)
                count = 1
        max_cnt = max(max_cnt,count)      
            
    return max_cnt
            
                
possible=[]

for i in range(N):
    for j in range(N - 1):
        # 가로로 인접한 두 사탕 교환
        if candy_map[i][j] != candy_map[i][j + 1]:
            tmp_map = deepcopy(candy_map)
            tmp_map[i][j], tmp_map[i][j + 1] = tmp_map[i][j + 1], tmp_map[i][j]
            possible.append(search(tmp_map))

for i in range(N - 1):
    for j in range(N):
        # 세로로 인접한 두 사탕 교환
        if candy_map[i][j] != candy_map[i + 1][j]:
            tmp_map = deepcopy(candy_map)
            tmp_map[i][j], tmp_map[i + 1][j] = tmp_map[i + 1][j], tmp_map[i][j]
            possible.append(search(tmp_map))

print(max(possible))
            
    