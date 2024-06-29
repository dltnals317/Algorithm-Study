function solution(polynomial) {
    const arr = polynomial.split(' ');
    var answer = '';
    var coefficient = 0
    var cst = 0
    arr.forEach((element)=>{
        if (element.includes("x")){
            val = element.slice(0,-1)
            if (val){
                coefficient+=parseInt(val)
            }
            else{
                coefficient+=1
            }
        }
        else if (element === "+"){
            return
        }
        else{
            cst+=parseInt(element)
        }
    })
    
    if (cst!==0 && coefficient===0){
        answer = String(cst)
    }
    else if (cst===0 && coefficient!==0){
        answer = coefficient!==1 ? String(coefficient)+"x" : "x"
    }
    else{
        answer = coefficient!==1 ? String(coefficient)+"x" +" + "+String(cst) : "x" +" + "+ String(cst)
    }
    
    return answer;
}



/*
polynomial돌면서, 직면할 수 있는건 4가지
1. 숫자
2. x
3. 공백
4. +

-공백을 기준으로 배열에 저장한다.
-배열을 돌면서, 해당 문자가 x를 포함하면 -> 문자를 맨 뒤 앞까지 슬라이싱하고 Coefficient+=계수
- 해당 문자가 x를 포함하지 않으면, 숫자이므로, cst +=수
- 해당 문자가 +이면 넘어가
*/