N,M,r,c,K = map(int,input().split())

dice_map = [list(map(int,input().split())) for _ in range(N)]
command = list(map(int,input().split()))
now_dice = [0,0,0,0,0,0]
#주사위 회전시키는 함수 (by 회전 )방향
def roll_dice(direction,now_dice):
    copy_dice = [0]*6
    if direction == 1: #동
        copy_dice[0],copy_dice[1],copy_dice[2],copy_dice[3],copy_dice[4],copy_dice[5] = now_dice[3],now_dice[1],now_dice[0],now_dice[5],now_dice[4],now_dice[2]

    elif direction == 2:
        copy_dice[0],copy_dice[1],copy_dice[2],copy_dice[3],copy_dice[4],copy_dice[5]= now_dice[2],now_dice[1],now_dice[5],now_dice[0],now_dice[4],now_dice[3]

    elif direction == 3:
        copy_dice[0], copy_dice[1], copy_dice[2], copy_dice[3], copy_dice[4], copy_dice[5] = now_dice[4], now_dice[0], now_dice[2], now_dice[3], now_dice[5], now_dice[1]
    else:
        copy_dice[0], copy_dice[1], copy_dice[2], copy_dice[3], copy_dice[4], copy_dice[5] = now_dice[1], now_dice[5], now_dice[2], now_dice[3], now_dice[0], now_dice[4]

    return copy_dice

def dice(r,c,command,dice_map,now_dice):
    new_dice = roll_dice(command,now_dice) #새로운 방향 제시
    # 방향: 동 서 북 남
    dr = [0, 0, 0, -1, 1]
    dc = [0, 1, -1, 0, 0]

    new_r = r+ dr[command]
    new_c = c + dc[command]

    if (0<=new_r<N and 0<=new_c<M):
        if dice_map[new_r][new_c] == 0: #이동한 칸에 쓰여 있는 수가 0이면
            dice_map[new_r][new_c] = new_dice[-1]
        else:
            new_dice[-1] = dice_map[new_r][new_c]
            dice_map[new_r][new_c] = 0
        return new_r, new_c, new_dice, dice_map,True
    else:
        return r, c, now_dice, dice_map, False


for com in command:
    r,c,now_dice,dice_map,moved = dice(r,c,com,dice_map,now_dice)
    if moved:
        print(now_dice[0])
