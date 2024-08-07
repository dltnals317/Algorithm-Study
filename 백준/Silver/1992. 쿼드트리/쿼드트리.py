def all_zero(two_matraix):
    for row in two_matraix:
        for element in row:
            if element != 0:
                return False
    return True

def all_one(two_matraix):
    for row in two_matraix:
        for element in row:
            if element != 1:
                return False
    return True

N = int(input())

entire = []
result_lst = []
for i in range(N):
    lst = list(map(int,input()))
    entire.append(lst)

def q_tree(two_matraix):
    size = len(two_matraix)//2
    if all_zero(two_matraix):
        result_lst.append(0)
        return
    if all_one(two_matraix):
        result_lst.append(1)
    
        
        return
    
    if size>1:
        result_lst.append("(")
        for i in range(0,len(two_matraix),size):
            for j in range(0,len(two_matraix[i]),size):
                sub_matrix = [row[j:j+size] for row in two_matraix[i:i+size]]
                q_tree(sub_matrix)
        result_lst.append(")")
            
    if size == 1:
        result_lst.append("(")
        for i in range(len(two_matraix)):
            for j in range(len(two_matraix[i])):
                result_lst.append(two_matraix[i][j])
        result_lst.append(")")

q_tree(entire)
print("".join(map(str,result_lst)))
