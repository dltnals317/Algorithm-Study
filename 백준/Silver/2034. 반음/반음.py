import sys
input = sys.stdin.readline

n = int(input())
melody = ["A",0,"B","C",0,"D",0,"E","F",0,"G",0] #건반을 리스트로 표현
distance_lst = []
tuple_lst = []
new_lst=[]
for i in range(n):
    value = int(input())
    distance_lst.append(value)

for value in melody: # ["A",0,"B","C",0,"D",0,"E","F",0,"G",0]
    if value == 0:
        continue
    idx = melody.index(value)
    for distance in distance_lst: #[-2, -1, -2, -2, -2, -1, -2]
        idx = (idx + distance)% len(melody) 
        if melody[idx] == 0:
            break
    tuple= (value,melody[idx])        
    tuple_lst.append(tuple)

for tuple in tuple_lst:
    if 0 not in tuple:
        new_lst.append(tuple)
        
for i in new_lst:
    for x in i:
        print(x,end=" ")
    print("")