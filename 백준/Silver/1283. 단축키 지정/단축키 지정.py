N = int(input())
word_lst = []
shortcuts= []
tup_lst = []
for _ in range(N):
    word_lst.append(input().split())


for lst in word_lst:
    for i in range(len(lst)):
        if lst[i][0].lower() not in shortcuts:
            shortcuts.append(lst[i][0].lower())
            tup_lst.append((lst[i][0],lst))
            lst[i] = lst[i].replace(lst[i][0],"[" + lst[i][0] + "]",1)
            
            print(" ".join(lst))
            break

    if lst not in tup_lst[-1]:
        for i,word in enumerate(lst):
            if lst not in tup_lst[-1]:
                #print("word",word)
                for char in word:
                    if char.lower() not in shortcuts:
                        shortcuts.append(char.lower())
                        tup_lst.append((char,lst))
                        word = word.replace(char,"[" + char + "]",1)
                        lst[i] = word   
                        print(" ".join(lst))
                        break     
                
    if lst not in tup_lst[-1]:
        tup_lst.append((-1,lst))
        print(" ".join(lst))
        