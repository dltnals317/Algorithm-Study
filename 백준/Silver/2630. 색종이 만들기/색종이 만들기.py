#입력 받아서 2차원 배열로 저장
"""
함수를 만들자
-역할 : 가로,세로를 반으로 나눠서, 새로운 정사각형 배열을 만든 후,
모두 1 혹은 모두 0 인지 판단한 후, 그게 아니라면, 다시 재귀적으로 해당 정사각형 배열을 인자로 넣어서 호출하는 함수
"""

N = int(input())

input_paper = []
for i in range(N):
    input_paper.append(list(map(int,input().split())))


def all_blue(two_matraix):
    for row in two_matraix:
        for element in row:
            if element != 1:
                return False
    return True

def all_white(two_matraix):
    for row in two_matraix:
        for element in row:
            if element != 0:
                return False
    return True

def devide_merge_paper(two_matrix_arr):

    # 기본 케이스: 1x1 배열
    if N == 1:
        if two_matrix_arr[0][0] == 1:
            return (0, 1)  # 흰색은 0개, 파란색은 1개
        else:
            return (1, 0)  # 흰색은 1개, 파란색은 0개
    
    top_left,top_right,bottom_left,bottom_right = [],[],[],[]
    mid = len(two_matrix_arr)//2
    for lst in two_matrix_arr[:mid]:
        top_left.append(lst[:len(lst)//2])
    for lst in two_matrix_arr[:mid]:
        top_right.append(lst[len(lst)//2:])
    for lst in two_matrix_arr[mid:]:
        bottom_left.append(lst[:len(lst)//2])
    for lst in two_matrix_arr[mid:]:
        bottom_right.append(lst[len(lst)//2:])
    
    blue = white = 0

    if all_blue(two_matrix_arr):
        blue += 1
    elif all_white(two_matrix_arr):
        white += 1
    else:
        sub_blue, sub_white = devide_merge_paper(top_left)
        blue += sub_blue
        white += sub_white
        sub_blue, sub_white = devide_merge_paper(top_right)
        blue += sub_blue
        white += sub_white
        sub_blue, sub_white = devide_merge_paper(bottom_left)
        blue += sub_blue
        white += sub_white
        sub_blue, sub_white = devide_merge_paper(bottom_right)
        blue += sub_blue
        white += sub_white

    return (blue, white)

blue, white = devide_merge_paper(input_paper)
print(white)
print(blue)