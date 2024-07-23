n = int(input())
word_dict = {}
word_set = set()

for i in range(n):
    word = input()
    length = len(word)    
    if length in word_dict.keys():
        word_dict[length].add(word)
    else:
        word_dict[length] = set()
        word_dict[length].add(word)
        


sorted_dict_1 = dict(sorted(word_dict.items())) # 딕셔러니 정렬방법

for key,value in sorted_dict_1.items():
    sorted_value = sorted(value)
    sorted_dict_1[key] = sorted_value
    


for key in sorted_dict_1.keys():
    for word in sorted_dict_1[key]:
        print(word)


