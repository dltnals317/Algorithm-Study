def solution(new_id):
    
    
    forbidden_string = ["~","!","@","#","$","%","^","&","*","(",")","=","+","[","{","]","}",":","?",",","<",">","/"]
    alpha = {
    'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 
    'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 
    'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 
    'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 
    'Y': 'y', 'Z': 'z'
}
    
    #step1 : 대문자 ->소문자
    for key,value in alpha.items():
        new_id = new_id.replace(key,value)
    
    # step2 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for x in new_id:
        if x in forbidden_string:
            new_id = new_id.replace(x,"")
    
    
     # step3 : new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if len(new_id)>0:
        if new_id[0] == "." :
            new_id = new_id[1:]
    if len(new_id)>0:
        if new_id[-1] == ".":
            new_id = new_id[:len(new_id)-1]
    #5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if len(new_id) == 0:
        new_id = 'a'
    
    #6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:14]
    #7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) <=2 :
        while len(new_id)!=3:
            x = new_id[-1]
            new_id = new_id + x
    return new_id