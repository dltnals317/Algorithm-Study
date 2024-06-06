R,C = map(int,input().split())
continent = []

#문자열을 리스트로 바꿔주기
for i in range(R):
    row = list(input())
    continent.append(row)

#좌,상,우,하
dx = [-1,0,1,0]
dy = [0,-1,0,1]

become_water = []
for y in range(R): #0,1,2,3,4
    for x in range(C): #0,1,2
        cnt = 0
        if continent[y][x] == ".":
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= ny < R and 0 <= nx < C:
                if continent[ny][nx] == ".":
                    cnt +=1
            else:
                cnt+=1
        if cnt >=3:
            become_water.append((y,x))


for y,x in become_water:
    continent[y][x] = "."

row_range = []
col_range = []
# 육지만 있는 땅으로 축소시키기
for i in range(R):
    if "X" not in continent[i]:
        continent
    else:
        j = continent[i].index("X")
        row_range.append(i)
        col_range.append(j)
        for j in range(C-1,-1,-1):
            if continent[i][j] == "X":
                col_range.append(j)
                break

min_row,max_row,min_col,max_col = min(row_range),max(row_range),min(col_range),max(col_range)


new_continent= []
continent = continent[min_row:max_row+1]
for lst in continent:
    lst = lst[min_col:max_col+1]
    new_continent.append(lst)


for i in range(len(new_continent)):
        print(''.join(new_continent[i]))
