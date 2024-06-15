# 1-2-3-1 만 가능
# 만들 수 있으면 cnt증가시키고 배열에서 제거해버리자
#idx를 돌면서, 가장 앞이 1인 경우, 이어지는 3묶음을 본다.(시간 단축)


def solution(ingredient):
    i = 0
    cnt=0
    while i<=len(ingredient) - 4:
        if ingredient[i:i+4] == [1,2,3,1]:
            cnt+=1
            del ingredient[i:i+4]
            i = max(0,i-3)
        else:
            i+=1
            
    
    return cnt