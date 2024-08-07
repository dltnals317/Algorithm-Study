sick = input()

group = []


group=sick.split("-")

result = 0
first = group[0]
if "+" in first:
    num_lst = first.split("+")
    num_lst = list(map(int,num_lst))
    first = sum(num_lst)
result+=int(first)
if len(group)!=1:
    for s in group[1:]:
        num_lst = s.split("+")
        num_lst = list(map(int,num_lst))
        minus_num = sum(num_lst)
        result -=minus_num


print(result)