sum_of_all = 0
dwarfs = []

# 입력 받기
for _ in range(9):
    height = int(input())
    dwarfs.append(height)
    sum_of_all += height

# 두 난쟁이의 합을 100으로 맞추기 위해 쌍을 찾기
found = False
for i in range(8):
    for j in range(i + 1, 9):
        if (sum_of_all - (dwarfs[i] + dwarfs[j])) == 100:
            # 두 난쟁이를 제거
            dwarfs.pop(j)  # j 번째 요소 제거
            dwarfs.pop(i)  # i 번째 요소 제거
            found = True
            break
    if found:
        break

# 결과를 오름차순으로 정렬 후 출력
dwarfs.sort()
for height in dwarfs:
    print(height)

    