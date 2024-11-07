#저번 문제처럼, 계층적으로 뭘 지워야하는 연산은 없다
#다만, 내가 가능하려면, 내 앞에(부모,부모의 부모)도 가능하도록 탐색하는 과정이 필요하겠군

# 한 부모에는 외동자식만 저장해두자(손자x)
# 어차피 내 외동자식의 외동자식이 손자니까

#스킬트리의 알파벳 하나씩을 탐색 -> 이게 스킬트리의 "value"에 있는지 확인(있다는건 부모가 있는거니까) -> 그렇다면 내 앞에 key가 있는지 확인(문자열 슬라이싱) ( 이 떄, 내가 맨 앞은 아닌지 조건 걸어주자-index에러 방지)
# 없다면, False로 바꾸기
#skill의 두 번째 원소부터 돌면서, 이전 인덱스를 참고하자


def solution(skill, skill_trees): 
    cnt=0
    graph = {}
    skill_split_lst= list(skill)
    for i in range(1,len(skill_split_lst)):
        parent,child = skill_split_lst[i-1],skill_split_lst[i]
        graph[parent] = child
    
    isSkillTreeLst = [False] *len(skill_trees)
    #스킬트리 탐색
    
    def validate_skill_tree(skill_tree):
        lst=list(skill_tree)
        for i,alpha in enumerate(lst):
            if i == 0:
                if alpha in graph.values(): #1번 인덱스면서 자식중에 있는거면,부모를 안거침
                    return False
                else:
                    continue
            else: #index가 0번이 아니면
                if alpha in graph.values(): 
                    prior_lst = lst[:i]
                    parent = [k for k,v in graph.items() if v == alpha][0]
                    if parent in prior_lst:
                        continue
                    else:
                        return False
                else:
                    continue
        return True
        
    for i,skill_tree in enumerate(skill_trees):
        b= validate_skill_tree(skill_tree)
        isSkillTreeLst[i] = b
        
    cnt=0
    for b in isSkillTreeLst:
        if b==True:
            cnt+=1
                
                
    
    return cnt