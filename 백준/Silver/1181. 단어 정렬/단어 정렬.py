n = int(input())
word_dict = {}

for _ in range(n):
    word = input().strip()
    length = len(word)
    if length in word_dict:
        word_dict[length].add(word)
    else:
        word_dict[length] = set()
        word_dict[length].add(word)

sorted_dict_1 = dict(sorted(word_dict.items()))

for key, value in sorted_dict_1.items():
    sorted_words = sorted(value)
    sorted_dict_1[key] = sorted_words

for key in sorted(sorted_dict_1.keys()):
    for word in sorted_dict_1[key]:
        print(word)

