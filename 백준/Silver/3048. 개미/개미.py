n1,n2 = map(int,input().split())
left = input()
left = left[::-1]
right = input()
T =int(input())
ants = [] # 각 개미의 (이름, 방향) 정보를 저장하는 리스트

for i in range(n1):
    ants.append((left[i],0))
for i in range(n2):
    ants.append((right[i],1))

if T == 0:
    result =[tup[0] for tup in ants]
    print(''.join(result))
else:
    for time in range(T):
        change_lst = set()
        for i,tup in enumerate(ants):
            if tup[1] == 1: #왼쪽으로 이동하는 개미들
                if i > 0 and ants[i-1][1] != 1:
                    change_lst.add((i-1,i))
                else:
                    continue
            elif tup[1] == 0: #오른쪽으로 이동하는 개미들
                if  i < len(ants) - 1 and ants[i+1][1] != 0:
                    change_lst.add((i,i+1))
                else:
                    continue
        for i,j in change_lst:
            ants[i],ants[j] = ants[j],ants[i]

    result =[tup[0] for tup in ants]
    print(''.join(result))
