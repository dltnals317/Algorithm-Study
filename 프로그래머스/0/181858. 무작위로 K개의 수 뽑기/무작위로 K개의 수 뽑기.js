function solution(arr, k) {
    var result = [];
    
    arr.forEach((num)=>{
        if (result.includes(num) === false && result.length < k){
            result.push(num)
        }
    })
    if (result.length < k){
        while(result.length < k){
            result.push(-1)
        }
    }
        
       
       
    return result;
}

/*
- arr를 돌면서, 숫자가 result에 없고 & result 배열 크기가 k보다 작으면 result배열에 넣는다
- result에 있으면 지나간다.
- arr를 다 돌았을 때, result의 길이 < k라면, result길이가 k가 될 때 까지 result에 -1넣는다

*/