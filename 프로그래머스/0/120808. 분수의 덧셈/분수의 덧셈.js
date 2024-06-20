function solution(numer1, denom1, numer2, denom2) {
    function greatestCommonDivisor(num1,num2){
        n = Math.min(num1,num2)
        while(1){
            if (num1 % n === 0 && num2 %n === 0){
            return n
        }
        else{
            n = n-1
        }
        }
    }
    var answer = [];
    denom = denom1*denom2
    numer = numer1*denom2 + numer2*denom1
    gcd = greatestCommonDivisor(numer,denom)
    console.log(gcd)
    answer = [numer/gcd , denom/gcd]
    
    
    return answer;
}

//1. 각각을 분수꼴로 만든다
//2. 분수를 덧셈한다
//3. 결과값을 기약분수로 만든다