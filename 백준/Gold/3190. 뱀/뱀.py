from collections import deque

N = int(input())
K = int(input())  # 사과 개수

snake_area = [[0] * N for _ in range(N)]
is_snake_body = [[False] * N for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    snake_area[r-1][c-1] = 1

L = int(input())  # 뱀의 방향 변환 횟수

change_dict = {}
for _ in range(L):
    timing_str, direction = input().split()
    timing = int(timing_str)
    change_dict[timing] = direction


def front_go(r, c, direction):
    if direction == 1:  # 뱀 머리가 ->동
        return (r, c + 1)
    elif direction == 2:  # 북
        return (r - 1, c)
    elif direction == 3:  # 남
        return (r + 1, c)

    else:  # 서
        return (r, c - 1)


# 방향 : 동(1),북(2),남(3),서(4)
def bfs_snake(r, c,direction):
    time = 0
    snake_q = deque([(r, c)]) #snake_q : 뱀의 몸통 영역이 해당하는 지점들
    is_snake_body[r][c] = True
    alive = True

    while alive:
        time+=1
        head_r,head_c = snake_q[-1]

        next_r, next_c = front_go(head_r, head_c, direction)  # 몸길이 늘려서 머리 위치시킨 곳
        if (0 <= next_r < N and 0 <= next_c < N and is_snake_body[next_r][next_c] == False): #종료 조건 아니면
            is_snake_body[next_r][next_c] = True
            snake_q.append((next_r,next_c)) #결국, 나아간 머리가 큐의 가장 끝에 들어가게 된다.
            if snake_area[next_r][next_c] == 1: #사과 만나면
                snake_area[next_r][next_c] = 0 #사과 없애기
                #꼬리는 안줄임

            else: #사과 안만나면
                tail_r, tail_c = snake_q.popleft()  # 큐에서 꼬리 제거(꼬리는 큐의 가장 앞에 위치)
                is_snake_body[tail_r][tail_c] = False  # 다시 뱀 영역이 아니게됨

            # 방향 바꾸는 타이밍인가?
            if time in change_dict.keys():
                if change_dict[time] == "L":
                    if direction == 1:
                        direction = 2
                    elif direction == 2:
                        direction = 4
                    elif direction == 3:
                        direction = 1
                    else:
                        direction = 3
                elif change_dict[time] == "D":
                    if direction == 1:
                        direction = 3
                    elif direction == 2:
                        direction = 1
                    elif direction == 3:
                        direction = 4
                    else:
                        direction = 2


        else:
            alive = False


    return time

result = bfs_snake(0,0,1)


print(result)