N = int(input())

student_dict = {}
for _ in range(N*N):
    student_info = list((map(int,input().split())))
    student_dict[student_info[0]] = student_info[1:]

#좌석 영역
sit_area = [[0]*N for _ in range(N)]


# 상,하,좌,우,
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def check_around(r,c,student_num): #r,c자리에서의 주변(좋아하는 친구,빈칸)파악
    absent = 0
    favorite = 0
    for i in range(4):
        n_r = r + dr[i]
        n_c = c + dc[i]

        if (0<=n_r<N and 0 <=n_c <N):
            if sit_area[n_r][n_c] == 0: #빈 좌석이면
                absent+=1
            else:
                if sit_area[n_r][n_c] in student_dict[student_num]:
                    favorite+=1
    return absent,favorite

def set_sit(student_num):

    candidate = []
    for r in range(N):
        for c in range(N):
            if sit_area[r][c] == 0: #빈자리면
                absent,favorite =check_around(r,c,student_num)
                candidate.append((favorite,absent,r,c))
    candidate.sort(key=lambda x: (-x[0], -x[1], x[2], x[3])) #-붙은게 "내림차순"정렬
    _,_,r,c = candidate[0]
    sit_area[r][c] = student_num



for order in student_dict.keys():
    set_sit(order)

score = [0,1,10,100,1000]
manjock = 0
for r in range(N):
    for c in range(N):
        student_num = sit_area[r][c]
        absent,favorit = check_around(r,c,student_num)
        manjock+= score[favorit]
print(manjock)