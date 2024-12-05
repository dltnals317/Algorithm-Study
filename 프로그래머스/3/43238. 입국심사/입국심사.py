def solution(n, times):
    answer = 0
    min_time = min(times) # 모든 인원 검사에 최소로 걸리는 시간
    max_time = max(times) * n   # 모든 인원 검사에 최대로 걸리는 시간

    while min_time <= max_time:
        
        # 처음에는 가장 오래 걸리는 시간과 가장 적게 걸리는 시간의 평균으로
        mid = (min_time + max_time) //2

        person_cnt = 0
        
        for time in times: #가장 적
            person_cnt += mid // time #총 걸리는 시간 // 한 사람 심사시 걸리는 시간 => 심사관이 담당하는 사람의 수

            # 모든 인원을 검사 가능 하면 break
            if person_cnt >= n:
                break

        # 모든 인원을 검사 가능하면 answer를 지금으로 업데이트 해주고
        # 최소 시간을 줄여나간다. high가 줄어들 수 있는 이상 최소값이 더 있을 수 있다.
        if person_cnt >= n :
            max_time = mid - 1
            answer= mid
        # 모든인원을 검사 할수 없으면 최소 시간을 늘린다.
        else :
            min_time = mid +1

    return answer