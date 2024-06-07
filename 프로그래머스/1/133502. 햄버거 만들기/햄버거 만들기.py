# 1-2-3-1 만 가능
# 만들 수 있으면 cnt증가시키고 배열에서 제거해버리자
#idx를 돌면서, 가장 앞이 1인 경우, 이어지는 3묶음을 본다.(시간 단축)


def solution(ingredient):
    cnt = 0
    i = 0

    while i <= len(ingredient) - 4:
        # 1-2-3-1 패턴을 찾으면
        if ingredient[i:i+4] == [1, 2, 3, 1]:
            # 패턴을 리스트에서 제거
            del ingredient[i:i+4]
            # 카운트 증가
            cnt += 1
            # i를 4만큼 뒤로 돌려서 같은 위치에서 다시 검사
            i = max(0, i - 3)
        else:
            # 패턴이 아닌 경우 다음 위치로 이동
            i += 1

    return cnt