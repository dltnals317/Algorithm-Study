from itertools import combinations

def cal_result(lst):
    sour = 1
    bitter = 0
    for gre in lst:
        sour *= gre[0]
        bitter += gre[1]
    return abs(sour-bitter)
    


N = int(input())
favor = []
result = []
for i in range(N):
    S,B = map(int,input().split())
    favor.append((S,B))

favor_combination=[]



for i in range(1,N+1):
    for comb in combinations(favor,i):
        favor_combination.append(comb)


for comb in favor_combination:
    value = cal_result(comb)
    result.append(value)

print(min(result))
    
    
        