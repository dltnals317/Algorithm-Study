import sys

input = sys.stdin.readline
N = int(input())
word_lst = []
for i in range(N):
    word = input()
    word_lst.append(word)
    
# for문 돌면서 

def group_word(word):
    finished = []
    for i in range(1,len(word)):
        if word[i] == word[i-1]:
            continue
        else:
            if word[i] in finished:
                return False
            else:
                finished.append(word[i-1])
               
    return True
cnt = 0        
for word in word_lst:
    v = group_word(word)
    if v == True:
        cnt+=1
print(cnt)
    
            
