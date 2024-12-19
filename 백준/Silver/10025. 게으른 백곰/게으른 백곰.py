N,K = map(int,input().split())


max_x = 0
bucket_lst = []

for _ in range(N):
    ice_num,x = map(int,input().split())
    bucket_lst.append([ice_num,x])
    if x>max_x:
        max_x = x

max_x+=1
# 배열의 최대 크기를 양동이의 최대 좌표로 설정
stock = [0]*max_x 

#얼음 양 기록
for i in range(N):
    ice_num , x = bucket_lst[i][0],bucket_lst[i][1]
    stock[x] = ice_num

#슬라이딩윈도우 초기화
window_size = 2*K + 1
current_sum = 0

for i in range(min(window_size,max_x)):
    current_sum+=stock[i]

max_ice_sum = current_sum

#슬라이딩윈도우 이동
for i in range(window_size,max_x):
    current_sum+=stock[i]
    current_sum-=stock[i-window_size]
    if current_sum > max_ice_sum:
        max_ice_sum = current_sum

print(max_ice_sum)
