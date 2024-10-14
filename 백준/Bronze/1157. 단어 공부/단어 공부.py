word = input().upper()
word_lst = list(set(word))
cnt_lst = []


for x in word_lst:
    cnt = word.count(x)
    cnt_lst.append(cnt)


max_cnt = max(cnt_lst)
if cnt_lst.count(max_cnt) >=2:
    print("?")
else:
    idx = cnt_lst.index(max_cnt)
    print(word_lst[idx])