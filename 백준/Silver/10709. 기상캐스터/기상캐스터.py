H,W = map(int,input().split())

sky_lst = []
distance_lst = [['.']*W for _ in range(H)]

for _ in range(H):
    row = list(input())
    sky_lst.append(row)


for i,sky in enumerate(sky_lst):
    last_cloud = (-1,-1)
    for j,spot in enumerate(sky):
        if spot == 'c':
            distance_lst[i][j] = 0
            last_cloud = (i,j)
        else: #spot == '.' 이면
            if last_cloud[1] == -1:
                distance_lst[i][j] = -1
            else:
                distance_lst[i][j] = j - last_cloud[1]

for lst in distance_lst:
    print(" ".join(map(str,lst)))
