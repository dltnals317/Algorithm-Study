sum = 0
lst = []
for i in range(9):
    x = int(input())
    lst.append(x)
    sum+=x

found = False
for i in range(8):
    for j in range(i+1,9):
        value = lst[i] + lst[j]
        if sum-value == 100:
            lst.pop(j)  # j 번째 요소 제거
            lst.pop(i)  # i 번째 요소 제거
            found = True
            break
    if found:
        break



lst.sort()
for x in lst:
    print(x)
    

    