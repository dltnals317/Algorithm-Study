function solution(n) {
    var answer = [];
    for (let i=2; i<n+1; i++) //i=2,3,4,5,6
        {
            if (n%i === 0)
                {
                    answer.push(i)
                    n = Math.floor(n / i)
                    
                }
        }
    fake_sosu = []
    for (let i = 0; i<answer.length; i++){
        for (let j = 2; j<answer[i]; j++){
            if (answer[i] % j === 0){
            console.log("가짜 소수", answer[i])
            fake_sosu.push(answer[i])
                break
        }
     
    }
        }
    
    for(let i=0;i<fake_sosu.length;i++){
        answer = answer.filter(num=>num!= fake_sosu[i])
    }
    return answer;
}



/*
-자기자신에서 1씩 감소하면서 (2까지), 나누어떨어지는게 있는지 확인 -> 
- 나누어떨어지는게 없다면, 자기 자신 리턴
-나누어떨어지는게 있다면, 자기자신을 몫으로 갱신 % 나누는 값 리스트에 넣기
*/