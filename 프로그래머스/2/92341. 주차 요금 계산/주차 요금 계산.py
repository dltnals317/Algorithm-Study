import math

def solution(fees, records):
    parking_info = {}  # 입차 시간을 저장할 딕셔너리
    time_info = {}     # 각 차량의 누적 주차 시간을 저장할 딕셔너리
    answer = []
    
    basic_time, basic_fee, per_time, per_fee = fees  # 요금 정책 분리
    
    # 1. 입/출차 기록 처리
    for record in records:
        time, car_num, state = record.split(" ")
        
        if state == "IN":  # 입차
            parking_info[car_num] = time  # 차량 번호에 입차 시간을 기록
        else:  # 출차
            in_time = parking_info.pop(car_num)  # 입차 시간 가져오기
            total_time = calculate_time(in_time, time)  # 입차 시간과 출차 시간 차이 계산
            
            if car_num not in time_info:
                time_info[car_num] = 0  # 처음 들어오는 차량은 초기화
            time_info[car_num] += total_time  # 누적 주차 시간 계산
    
    # 2. 출차 기록이 없는 차량 처리
    for car_num, in_time in parking_info.items():
        total_time = calculate_time(in_time, "23:59")  # 출차 없이 23:59에 출차 처리
        if car_num not in time_info:
            time_info[car_num] = 0
        time_info[car_num] += total_time
    
    # 3. 요금 계산
    for car_num in sorted(time_info.keys()):
        total_time = time_info[car_num]
        fee = calculate_fee(total_time, basic_time, basic_fee, per_time, per_fee)
        answer.append(fee)
    
    return answer

# 시간을 계산하는 함수 (입차 시간과 출차 시간의 차이를 분 단위로 계산)
def calculate_time(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(":"))
    out_hour, out_minute = map(int, out_time.split(":"))
    return (out_hour * 60 + out_minute) - (in_hour * 60 + in_minute)

# 요금을 계산하는 함수 (기본 요금 + 초과 시간에 따른 추가 요금 계산)
def calculate_fee(total_time, basic_time, basic_fee, per_time, per_fee):
    if total_time <= basic_time:
        return basic_fee
    else:
        extra_time = total_time - basic_time
        extra_fee = math.ceil(extra_time / per_time) * per_fee
        return basic_fee + extra_fee
