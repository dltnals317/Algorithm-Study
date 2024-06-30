function solution(num, total) {
    var result = []
    var answer = [];
     if(num === 1){
        return [total];
    }
    for(let i = Math.max(num,total); i>0; i--){
        var sum = 0
        for (let j =0; j<num;j++){
            sum+= (i-j)
        }
         if (sum === total){
            for (let k =0; k<num;k++){
            result.push(i-k)
        }
         }       
    }
    answer = result.sort((a,b)=>a-b)
    return answer;
}