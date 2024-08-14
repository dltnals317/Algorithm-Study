N, M = map(int, input().split())

no_hear = set()
for _ in range(N):
    name = input()
    no_hear.add(name)

no_see = set()
for _ in range(M):
    name = input()
    if name in no_hear:
        no_see.add(name)

# 결과를 정렬하여 출력
result_list = sorted(no_see)
print(len(result_list))
for name in result_list:
    print(name)
