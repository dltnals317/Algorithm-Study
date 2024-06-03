#제일 뒤에서부터 기준점
# 내 앞에애가, 문자열 내에 존재하고  and 그 인덱스가 나보다 작을 때
# 내 앞에애가 문자열 내에 존재하지 않으면, 또 그 앞 애를 보기
# 기준을 내 앞에 애로



def solution(skill, skill_trees):
    cnt=0
    for word in skill_trees:
        lst = []
        course_lst = [ char for char in word if char in skill ]
        print(course_lst)
        for i in range(len(skill)):
            if skill[i] not in course_lst:
                continue
            else:
                if i == course_lst.index(skill[i]):
                    lst.append(True)
                else:
                    lst.append(False)
        if False not in lst:
            cnt+=1
            
        answer = cnt
    return answer