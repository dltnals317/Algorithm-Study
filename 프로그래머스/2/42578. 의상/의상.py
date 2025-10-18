from collections import Counter

def solution(clothes):
    count_by_type = Counter([kind for name, kind in clothes])
    answer = 1
    for cnt in count_by_type.values():
        answer *= (cnt + 1)  # 선택하거나 안 선택하거나
    return answer - 1
