def perm(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]  # 현재 i를 제외한 나머지
        for p in perm(rest, n - 1):  # 나머지 중에서 n-1 뽑기
            result.append([arr[i]] + p)
    return result


n, k = map(int, input().split())
a_lst = list(map(int, input().split()))

possible_lst = perm(a_lst, n)

cnt = 0

for i in range(len(possible_lst)):
    power = 500
    for p in possible_lst[i]:
        power += p - k
        if power < 500:
            break
    else:  # break 없이 루프가 끝난 경우
        cnt += 1

print(cnt)
