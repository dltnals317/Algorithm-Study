function solution(str_list) {
    var answer = [];
    l_idx = 0
    r_idx = 0
    for (let i = 0; i<str_list.length; i++)
        {
            if (str_list[i] === "l")
                {
                    l_idx = i
                    answer = str_list.slice(0,l_idx)
                    break
                }
            else if (str_list[i] === "r")
                {
                    r_idx = i
                    answer = str_list.slice(r_idx+1)
                    break
                }
            else
            {
                continue
            }
        }
    
           
    return answer;
}

/*
for문을 돌면서, 값이 ㅣ도 아니고, r도 아닐 때, 계속 돈다
for문을 돌면서, 값이 ㅣ이나 r일 때, 해당 인덱스를 기록하고 반복문 종료
str_lst에서 기록해둔 인덱스 기준으로 슬라이싱
*/