"""
 각 트럭의 주차 시작 시간과 끝 시간을 리스트에 저장
 최대 주차 시간을 계산하여 그 크기만큼 리스트를 생성하고, 각 시간대에 주차된 트럭 수를 기록.
 이후, 각 시간대에 주차된 트럭 수에 따라 요금을 계산하여 합산. 
 마지막으로 총 주차 요금을 출력.
"""

A,B,C = map(int,input().split())

time = []
for i in range(3):
    start,end = map(int,input().split())
    time.append((start,end))
    
max_t = max(time[0][-1],time[1][-1],time[2][-1])


parking = [[] for _ in range(max_t)]

for idx,tup in enumerate(time):
    start,end = tup[0],tup[1]
    for i in range(start,end):
        parking[i-1].append(1)

cost = 0


for lst in parking:
    if len(lst) == 1:
        cost += A
        
    elif len(lst) == 2:
        cost +=B*2
        
    elif len(lst) == 3:
        cost+=C*3
print(cost)
        
