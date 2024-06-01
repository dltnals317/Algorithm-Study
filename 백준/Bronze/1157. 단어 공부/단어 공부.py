word = input()
def find_max_char(word):
    word= word.upper()
    word_dict = {}
    max_cnt = 0
    for char in word:
        if char in word_dict.keys():
            word_dict[char] +=1
        else:
            word_dict[char] = 1
    
    max_cnt = max(word_dict.values())
    max_char = [char for char,count in word_dict.items() if count == max_cnt]

    if len(max_char) > 1:
        return "?"
    else:
        return max_char[0]     
    
rst = find_max_char(word)
print(rst)
    