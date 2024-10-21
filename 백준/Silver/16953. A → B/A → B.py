"""

1. B의 맨 끝이 1이라면 => 무조건 이전 연산은 1을 붙이는 것

2. B의 맨 끝이 1이 아니라면 => 무조건 이전 연산은 2를 곱한 것


B를 계속 초기화 (a가 될 때까지)
"""


A,B = input().split()


cnt=0

while (B != A):
    last = B[-1]
    if last == "1":
        B = B[:len(B)-1]
       
    else:
        if int(B)%2 != 0:
            cnt = -2
            break
        else:
            B = int(B)//2   
            B = str(B)
    cnt+=1

    if int(B)<int(A):
        cnt = -2
        break
    

print(cnt+1)