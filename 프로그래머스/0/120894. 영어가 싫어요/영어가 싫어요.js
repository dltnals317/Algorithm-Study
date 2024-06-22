function solution(numbers) {
    var answer = 0;
    var eng = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3, 
        'four': 4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9
    };
    
    for(const [key,value] of Object.entries(eng)){
        if (numbers.includes(key)){
            numbers = numbers.replaceAll(key,value)
            console.log(numbers)
        }
    }
    answer = parseInt(numbers)
    return answer;
}

//영어사전 object만들기
//