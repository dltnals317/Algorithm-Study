def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for c in s:
            if 48<=ord(c)<=57:
                continue
            else:
                return False
        return True
    else:
        return False
    