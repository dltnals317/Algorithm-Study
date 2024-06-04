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
        