def solution(numbers):
    # 각 숫자를 세 번씩 이어붙인 문자열을 기준으로 정렬하여 가장 큰 수를 만듦
    sorted_numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(sorted_numbers)))  # 정렬된 문자열을 합쳐서 정수로 변환한 후 다시 문자열로 변환
    
    return answer

# 예시 호출
numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]
print(solution(numbers1))  # 출력: "6210"
print(solution(numbers2))  # 출력: "9534330"


