n = int(input())
import sys
input = sys.stdin.readline
time_dict={}
time_lst= list(map(int,input().split()))
added_time = [0] * (n+1)
for i in range(len(time_lst)):
    time_dict[i+1]=time_lst[i]

sorted_time_dict = dict(sorted(time_dict.items(),key=lambda x:x[1]))
#time_dict를 값에 따라 작은 순서대로 정렬한 후에 이를 리스트로 반환


for index,(key,value) in enumerate(sorted_time_dict.items()):
    for i in range(index+1,len(added_time)):
        added_time[i]+=value

total_time=0
for time in added_time:
    total_time+=time

print(total_time)
    