def check(lst):
    stack = []
    for x in lst:
        if x == "(":
            stack.append(x)
        elif x == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack)>0:
        return False
    return True
            


def solution(s):
    lst = list(s)
    result = check(lst)
        

    return result