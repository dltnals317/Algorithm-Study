"""
1) 1 -> 묶지 않는게 좋음
2) (-) -> 작은 수(절대값 큰 수)끼리 묶는게 좋음
       -> 음수 한개와 0을 묶음
"""
            




n = int(input())
num_lst = []
for _ in range(n):
    num = int(input())
    num_lst.append(num)


positive = []
negative = []
one_cnt = 0
zero_cnt = 0

for num in num_lst:
    if num>1:
        positive.append(num)
    elif num == 1:
        one_cnt+=1
    elif num == 0:
        zero_cnt+=1
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

result = 0
for i in range(0,len(positive)-1,2):
    result+=positive[i]*positive[i+1]


if len(positive) % 2 == 1: #길이가 홀수면 하나 남음
    result += positive[-1]
    

for i in range(0, len(negative)-1, 2):  
    result += negative[i] * negative[i+1]

if len(negative)%2 == 1:
    if zero_cnt>0:
        result+=0
    else:
        result += negative[-1]

result+=one_cnt

print(result)
    