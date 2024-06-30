function solution(sides) {
    var answer = 0;
    var result = []
    sum = sides[0] + sides[1]
    
    for(let i = sum-1; Math.max(sides[0],sides[1])<i;i--){
        result.push(i)
    }
    
    var largest = Math.max(sides[0],sides[1])
    var min = Math.min(sides[0],sides[1])
    
    for (let i = largest; i>largest-min; i--){
        result.push(i)
    }
    console.log(result)
    answer = result.length
    return answer;
}



/*
1. 가장 긴 변이 주어진 sides중 큰 값일 경우
-> 새로 추가되는 변 x 라고 하면, min+x > max 이므로, max=>x>max-min
2. 가장 긴 변이 아직 안주어진 경우

- 

*/