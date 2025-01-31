from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))  # (현재 합, 탐색 횟수)
    answer = 0

    while queue:
        current_sum, count = queue.popleft()

        # 모든 숫자를 사용한 경우
        if count == len(numbers):
            if current_sum == target:
                answer += 1
            continue

        # 다음 숫자를 더하거나 빼는 경우의 수 추가
        queue.append((current_sum + numbers[count], count + 1))
        queue.append((current_sum - numbers[count], count + 1))

    return answer
