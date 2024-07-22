def get_start_time(end_time, process_time):
    # 시간을 시, 분, 초로 분리
    hh_mm_ss = end_time.split(":")
    hour, minute, second = int(hh_mm_ss[0]), int(hh_mm_ss[1]), float(hh_mm_ss[2])
    
    # 처리 시간을 초 단위로 변환
    processing_time = float(process_time[:-1])
    
    # 시작 시간 계산 (응답 완료 시간 - 처리 시간 + 0.001초)
    end_time_in_seconds = hour * 3600 + minute * 60 + second
    start_time_in_seconds = end_time_in_seconds - processing_time + 0.001
    
    return start_time_in_seconds

def convert_to_seconds(time_str):
    hh, mm, ss = time_str.split(":")
    return int(hh) * 3600 + int(mm) * 60 + float(ss)

def solution(lines):
    times = []
    
    for log in lines:
        lst = log.split(" ")
        end_time = lst[1]
        process_time = lst[2]
        
        end_time_in_seconds = convert_to_seconds(end_time)
        start_time_in_seconds = get_start_time(end_time, process_time)
        
        times.append((start_time_in_seconds, end_time_in_seconds))
    
    max_traffic = 0
    
    for i in range(len(times)):
        # 현재 로그의 종료 시간을 기준으로 1초 구간
        start_time_window = times[i][0]
        end_time_window = times[i][1]
        
        start_count = sum(1 for start, end in times if start < start_time_window + 1 and end >= start_time_window)
        end_count = sum(1 for start, end in times if start < end_time_window + 1 and end >= end_time_window)
        
        max_traffic = max(max_traffic, start_count, end_count)
    
    return max_traffic