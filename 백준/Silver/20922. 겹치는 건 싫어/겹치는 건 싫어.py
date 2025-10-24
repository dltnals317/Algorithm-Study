from collections import defaultdict

n,k = map(int,input().split())
arr = list(map(int,input().split()))


cnt_dict = defaultdict(int)

start_idx,end_idx = 0,0

arr_len = len(arr)
max_len = 0
while(start_idx<arr_len and end_idx<arr_len):
  now = arr[end_idx]
  if cnt_dict[now]<k:
    cnt_dict[now] +=1
    end_idx +=1
    max_len = max(max_len, end_idx - start_idx)
  else:
    deleted = arr[start_idx]
    cnt_dict[deleted] -=1
    start_idx +=1
      
      
  
print(max_len)