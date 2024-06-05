# 2차원 배열로 만들어
# 처음으로 #가 등장하는 행이, 시작점 lux가 되고,
#마지막으로 #가 등장하는 행 + 1이, 끝 점 rdx가 된다

# 각 행마다, #가 가장 왼쪽으로 치우친거 luy 
# #가 가장 오른쪽으로 치우친거+1 = rdy

def solution(wallpaper):
    
    for i in range(len(wallpaper)):
        wallpaper[i]=list(wallpaper[i])
    
    col = len(wallpaper[0])
    print("col",col)
    for i in range(len(wallpaper)): #시작 x
        if "#" in wallpaper[i]:
            lux = i
            break
    for i in range(len(wallpaper)-1,-1,-1): #끝 x
        if "#" in wallpaper[i]:
            rdx = i+1
            break
    col_file=[]
    for i in range(len(wallpaper)):
        if "#" in wallpaper[i]:
            for j in range(len(wallpaper[i])):
                if wallpaper[i][j] == "#":
                    col_file.append(j)
                    print("#_idx",j)
    print("col_file",col_file)
    luy = min(col_file)
    rdy = max(col_file) + 1
    
    answer = [lux,luy,rdx,rdy]
    return answer