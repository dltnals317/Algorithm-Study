function solution(s) {
    var answer = 0;
    //배열의 탐색
    let lst = s.split(" ");  //문자열을 공백을 기준으로 리스트에 담는 문법
    let tmp = 0
    for (i=0;i<lst.length;i++){
        if (lst[i] !== 'Z'){
            answer +=  parseInt(lst[i])
            tmp =  parseInt(lst[i])
        }
        else if (lst[i] === 'Z'){
            answer -= tmp
        }
    }
    return answer;
}


//배열을 탐색하면서, 더한다. 이 때, 이전 값을 저장한다
//Z를 만나면 이전 값을 뺀다
// 숫자를 만나면 이전 값을 더한다
