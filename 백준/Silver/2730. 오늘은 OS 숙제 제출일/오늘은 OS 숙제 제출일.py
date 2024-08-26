# 월별 일수와 윤년 처리
thirty_days_month = [4, 6, 9, 11]
thirty_one_days_month = [1, 3, 5, 7, 8, 10, 12]

def days_in_month(month, year):
    if month in thirty_days_month:
        return 30
    elif month in thirty_one_days_month:
        return 31
    else:  # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28

def date_to_days_total(day, month, year):
    days = 0
    # Add days for years
    for y in range(1, year):
        days += 366 if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else 365
    # Add days for months in the current year
    for m in range(1, month):
        days += days_in_month(m, year)
    # Add days in the current month
    days += day
    return days

def datetime_to_string(month, day, year):
    # Convert to string without leading zeros
    return f'{month}/{day}/{year}'

def handle_dates(deadline_str, submission_str):
    d_month, d_day, d_year = map(int, deadline_str.split('/'))
    s_month, s_day = map(int, submission_str.split('/'))
    
    # 마감일과 제출일을 일수로 변환
    total_deadline = date_to_days_total(d_day, d_month, d_year)
    
    # 제출일의 연도를 추정하여 두 가지 경우를 처리
    possible_years = [d_year - 1, d_year, d_year + 1]
    closest_submission_date = None
    closest_gap = float('inf')
    
    for year in possible_years:
        total_submission = date_to_days_total(s_day, s_month, year)
        gap = total_submission - total_deadline
        if abs(gap) < abs(closest_gap):
            closest_gap = gap
            closest_submission_date = (s_month, s_day, year)
    
    # 날짜 차이 계산
    s_month, s_day, s_year = closest_submission_date
    gap = closest_gap
    
    if gap > 0:
        if 1 < gap <= 7:
            return f'{datetime_to_string(s_month, s_day, s_year)} IS {gap} DAYS AFTER'
        elif gap == 1:
            return f'{datetime_to_string(s_month, s_day, s_year)} IS {gap} DAY AFTER'
        else:
            return "OUT OF RANGE"
    elif gap < 0:
        gap = -gap
        if 1 < gap <= 7:
            return f'{datetime_to_string(s_month, s_day, s_year)} IS {gap} DAYS PRIOR'
        elif gap == 1:
            return f'{datetime_to_string(s_month, s_day, s_year)} IS {gap} DAY PRIOR'
        else:
            return "OUT OF RANGE"
    else:
        return "SAME DAY"

# 입력을 처리하는 부분
N = int(input())
results = []

for _ in range(N):
    deadline, submission = input().split()
    result = handle_dates(deadline, submission)
    results.append(result)
    
# 결과 출력
for result in results:
    print(result)
