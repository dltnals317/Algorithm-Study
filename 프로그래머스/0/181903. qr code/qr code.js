function solution(q, r, code) {
    var answer = '';
    
    let code_lst = [...code]
    
    code_lst.map((item,i)=>{
        if(i%q === r)
            {
                answer+=item
            }
    })
    
    return answer;
}


/*
1. 문자열을 배열로 변환하기
2. map함수를 써서, 각각 배열 값에 q로 나눈 나머지를 새로운 배열로 저장하기(람다함수처럼)
3. new배열을 돌면서, r과 같은 값의 인덱스를 가지고 기존 배열에서 값을 꺼낸 후, 그것들을 이어붙인다.

*/