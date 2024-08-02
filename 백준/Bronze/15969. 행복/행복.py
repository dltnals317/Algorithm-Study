N = int(input())
grade = list(map(int,input().split()))
result = max(grade)-min(grade)
print(result)