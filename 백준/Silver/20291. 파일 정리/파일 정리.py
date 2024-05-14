import sys
input = sys.stdin.readline
file_lst = []
extension_dict = {}
def arrange_system(file_lst):
    for file in file_lst:
        idx = file.find(".")
        extension = file[idx+1:]
        if extension not in extension_dict.keys():
            extension_dict[extension] = 1
        else:
            extension_dict[extension]+=1

    result = sorted(extension_dict.items())
    return result    


n = int(input())
file_lst = []
for i in range(n):
    file = input().strip()
    file_lst.append(file)

result = arrange_system(file_lst)

for item in result:
    print(item[0],item[1])