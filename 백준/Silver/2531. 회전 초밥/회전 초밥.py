from collections import defaultdict
n,d,k,c = map(int,input().split())

belt = [int(input()) for _ in range(n)] 


left, right = 0,0
dup = defaultdict(int)


#초기 슬라이드 윈도우
for i in range(k):
    dup[belt[i]] +=1 #left_idx=0, right_idx=k-1인 상태

max_cnt = len(dup) + (1 if c not in dup else 0) #서로 다른 초밥 개수

for i in range(1,n): #i=1...N-1
    left = belt[i-1] #기존 슬라이딩 윈도우에서 가장 왼쪽에 있던
    dup[left] -=1 # 개수 -=1

    if dup[left] == 0: #기존에 중복된 상황이 아니었다면
        del dup[left]
  
    right = belt[(i-1+k) % n]
    dup[right]+=1

    current = len(dup) + (1 if c not in dup else 0)
    max_cnt = max(max_cnt,current)
print(max_cnt)