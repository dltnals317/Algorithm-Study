# skill에 해당하는 코스만 리스트 컴프리헨션으로 리스트를 구성한뒤,
#skill의 char를 돌면서, 그것의 인덱스 i == course_lst.index(skill[i])이면
#즉,  course_lst.index(skill[i])는 내 앞에 있는 코스의 수인데, 이것과 i가 같으면 True를 넣는 식



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
