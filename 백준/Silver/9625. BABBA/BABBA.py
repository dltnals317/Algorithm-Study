K = int(input())

a_count=[0]*(K+1)
b_count=[0]*(K+1)
a_count[0] = 1
b_count[0] = 0
a_count[1] = 0 #1번 버튼 눌렀을 때, a의 갯수
b_count[1] = 1

for i in range(2,K+1):
    a_count[i] = a_count[i-1] + a_count[i-2]
    b_count[i] = b_count[i-1] + b_count[i-2]

print(a_count[-1],b_count[-1],end=" ")
