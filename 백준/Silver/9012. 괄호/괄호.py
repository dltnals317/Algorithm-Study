T = int(input())

def vps(lst):
    stack = []
    if lst[0] == ")":
        return("NO")
    else:
        for i in range(len(lst)):
            if len(stack) == 0:
                stack.append(lst[i])
               
            else:
                if lst[i] == stack[-1]:
                    stack.append(lst[i])
                    
                else:
                    last = stack.pop()
                    
                    value = last + lst[i]
                    if value == "()":
                        continue
                    else:
                        return("NO")
    if stack:
        return("NO")
    else:
        return("YES")

 


for i in range(T):
    lst=list(input())
    result = vps(lst)
    print(result)
    